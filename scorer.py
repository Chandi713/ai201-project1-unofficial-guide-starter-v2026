import re
from pathlib import Path

from ingest import clean_text


STOPWORDS = {
    "a", "an", "am", "and", "are", "as", "at", "be", "but", "by",
    "do", "does", "for", "from", "if", "in", "is", "it", "like",
    "not", "of", "on", "or", "the", "to", "was", "were", "with", "you",
}

SOURCE_DIR = Path(__file__).parent / "corpora" / "advice_threads" / "documents"


def _clean_text(data: str) -> set[str]:
    words = re.findall(r"[a-z0-9]+", data.lower())
    return {word for word in words if word not in STOPWORDS}


def _names_source(answer: str) -> bool:
    cited_sources = re.findall(r"\b[a-z0-9_-]+\.txt\b", answer, re.IGNORECASE)
    if not cited_sources:
        return False

    actual_sources = {path.name.lower() for path in SOURCE_DIR.glob("*.txt")}
    return all(source.lower() in actual_sources for source in cited_sources)


def _contains_complete_document(result) -> bool:
    source_path = SOURCE_DIR / result.source
    if not source_path.is_file() or source_path.parent != SOURCE_DIR:
        return False

    document_text = clean_text(source_path.read_text(encoding="utf-8"))
    # print(f"Document Text: {document_text}")
    # print(f"\nResult Text: {result.text}")
    return clean_text(result.text) == document_text


def compare_expectation(expects: str, results) -> bool:
    expected_words = _clean_text(expects)
    if not expected_words:
        return False

    # print("Expectation: ", expects)
    # print("Expected Words: ", expected_words)
    matching_chunks = 0
    chunk_count = 0
    for result in results:
        chunk_count += 1
        chunk_words = _clean_text(result.text)
        # print(f"Chunk-{chunk_count}: {result}")
        # print("Chunk Wrods: ", chunk_words)
        matched_words = expected_words & chunk_words
        # print("Matched Wrods: ", matched_words)
        coverage = len(matched_words) / len(expected_words)
        # print("Coverage: ", coverage)
        # print("\n")

        if coverage >= 0.7:
            matching_chunks += 1

    return matching_chunks >= 1


def _answer_has_acceptable_length(answer: str) -> bool:
    token_count = len(re.findall(r"\b[a-z0-9]+\b", answer.lower()))
    return 5 <= token_count <= 90


def judge(question: str, expects: str, answer: str, results) -> bool:
    passed = compare_expectation(expects, results)
    source_passed = _names_source(answer)
    complete_chunks = sum(_contains_complete_document(result) for result in results)
    answer_length_passed = _answer_has_acceptable_length(answer)

    criteria = [
        ("C1", "Retrieved chunks contain the answer", passed),
        ("C2", "Answer names a valid source", source_passed),
        ("C4", "Retrieved chunks contain complete documents", bool(complete_chunks)),
        ("C5", "Answer length is between 5 and 90 words", answer_length_passed),
    ]
    passed_count = sum(result for _, _, result in criteria)

    print(f"Question: {question}")
    for code, description, _ in criteria:
        print(f"- {code}: {description}")
    overall_verdict = "PASS" if passed_count >= 3 else "FAIL"
    print(
        "Verdicts: "
        + " | ".join(
            f"{code}: {'PASS' if result else 'FAIL'}"
            for code, _, result in criteria
        )
        + f" | Total: {passed_count}/4 | Overall: {overall_verdict}"
    )

    return passed_count >= 3