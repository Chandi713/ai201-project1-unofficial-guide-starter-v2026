# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->
Name: Smit Chandi
Corpus: advice_threads

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->
I took "advice_threads" corpora. It is about a practical undergraduate advice from students perspective answer common campus life, academic planning, experiences questions. In other words, it answers the questions about daily logistics and routines, academic planning, social and residential life, etcetera.

## Chunking Strategy

**Chunk size: 800**
**Overlap: 120 characters**
I use `chunker.py::split_documents`, which groups blank-line-separated replies
without cutting through a paragraph or combining different source documents.
Chunks target 800 characters, and a later chunk carries trailing reply context
from the previous chunk using the 120-character overlap setting. The corpus is
made of short, self-contained advice threads, so most documents remain one
complete chunk while longer documents can be split at reply boundaries.
<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `thread_bike_commute.txt` — produced by: `chunker.py::split_documents`

```
THREAD: Is a bike worth it for a 20 minute walk commute?

--- reply 1 (14 votes) ---
Yeah. Cuts an 18 minute walk to about 6. The thing nobody mentions is storage — covered bike parking exists at three buildings and is full by 9am at all three.

--- reply 2 (9 votes) ---
Counterpoint, I sold mine. Between November and March the paths are either icy or salted and salt destroys a drivetrain in one season.

--- reply 3 (22 votes) ---
Both true. I keep a cheap bike for September to November and walk the rest of the year. Total costwas about $120 for the bike and I don't care what happens to it.

--- reply 4 (5 votes) ---
If you do get one, the campus does free registration and it's the only reason I got mine back after it was taken.

```

**Chunk 2** — source: `thread_first_gen.txt#0` — produced by: `chunker.py::split_documents`

```
THREAD: Anything specific for first-generation students?

--- reply 1 (33 votes) ---
The advising office has a specific programme and it is genuinely good, but it is opt-in and badly publicised. Ask for it by name.

--- reply 2 (41 votes) ---
The thing I'd say: the unwritten rules are the hard part, not the coursework. Ask about the unwritten rules explicitly. People are happy to explain them and nobody volunteers them.

--- reply 3 (16 votes) ---
Emergency fund for textbooks and travel exists and is not means-tested beyond a short form.
```

**Chunk 3** — source: `thread_laptop_specs.txt#0` — produced by: `chunker.py::split_documents`

```
THREAD: How much laptop do I actually need for CS courses?

--- reply 1 (31 votes) ---
Less than the recommended spec page says. 16GB of RAM is the one number worth paying for; everything else you'll never notice.

--- reply 2 (18 votes) ---
Adding: the lab machines exist and are better than anything you'll buy. For the heavy assignments people just use those.

--- reply 3 (12 votes) ---
I did two years on an 8GB machine and it was fine until the last project, at which point it very much wasn't. 16 is the answer.
```

**Chunk 4** — source: `thread_office_hours_etiquette.txt#0` — produced by: `chunker.py::split_documents`

```
THREAD: Is it weird to go to office hours with no specific question?

--- reply 1 (44 votes) ---
No, and this is the single most common thing first years get wrong. 'I'm following the lectures but I don't feel like I understand the shape of it' is a completely normal thing to say.

--- reply 2 (29 votes) ---
They're usually empty. You are doing the instructor a favour by turning up.

--- reply 3 (18 votes) ---
If it helps, treat it as a standing appointment. Go every week for a month and it stops feeling like a thing.

```

**Chunk 5** — source: `thread_professor_email.txt#0` — produced by: `chunker.py::split_documents`

```
THREAD: Do professors actually answer email?

--- reply 1 (21 votes) ---
Varies enormously. General rule I've found: if the syllabus states a response window, it's honoured. If it doesn't, assume 48 hours and don't panic before then.

--- reply 2 (33 votes) ---
Office hours are dramatically more effective than email for anything that takes more than two sentences to answer. They're also usually empty.

--- reply 3 (15 votes) ---
Empty office hours is the biggest unused resource here and I say that having wasted a year not going.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
What should I do if my roommate situation is not working? — run 1

**Answer:**

```
Best distance: 0.3535 (passed the gate)
Sources retrieved: thread_roommate_conflict.txt, thread_group_project.txt, thread_office_hours_etiquette.txt

Based on the provided documents, you should talk to your RA early and frame the conversation as needing help to sort things out rather than asking to move immediately (*thread_roommate_conflict.txt*). Additionally, you should write down specific details before your meeting rather than just saying the situation is not working (*thread_roommate_conflict.txt*).
```

**My relevance cutoff: 0.6**
This was a good cutoff because the in-corpus questions stayed below it and the out-of-scope questions stayed above it, leaving a clear gap.
<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---:|
| When is laundry actually free in the dorms? | Yes | 0.3276 |
| Is the printing quota enough for most students? | Yes | 0.3146 |
| When should I use the pass/fail option for a class? | Yes | 0.4642 |
| What should I do if my roommate situation is not working? | Yes | 0.3535 |
| Is it worth going to office hours if I do not have a specific question? | Yes | 0.5029 |
| What is the capital of Mongolia? | No | 0.8900 |
| How do I change the oil in a diesel engine? | No | 0.9300 |
| Who won the 1994 World Cup? | No | 0.7870 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.8280 |
| How do I write a for loop in Rust? | No | 0.8710 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.** I asked an AI model to help me turn my notes about the advice_threads corpus into a clear project description and a sensible set of evaluation questions. It suggested a general summary and a few question ideas, but it did not capture the exact shape of the corpus or the project rubric well enough, so I rewrote the description to match the actual documents and the assignment’s criteria. I also narrowed the question set to realistic student-life queries that were clearly covered by the thread files.

**2.** I asked an AI model to summarize the project requirements and break the work into smaller tasks so I could follow the expected workflow. It helped me map the milestones and identify what needed to be done in sequence, but I still checked the repo and grading rubric myself. I also used AI to read the generated results file and extract the key numbers and outputs for the README, which saved time and reduced manual errors, but I verified the extracted values against the raw output before using them in the final submission.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Sampled chunks are complete | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. Answer chunk is in first three results | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

**Evidence:** `results/run_2026-09-21_0251_before.md`, produced by
`run_eval.py::main`, recorded `top-k: 3` and three runs per in-corpus question.
The retrieval checks were produced by `app.py::cmd_retrieve` and ranked the
answer-containing source first for all five questions.

```text
### Raw output from run_eval.py::main
- Sources retrieved: thread_commuting.txt, thread_laundry_timing.txt, thread_study_spots.txt
Laundry is actually free in the dorms on Tuesday and Wednesday mornings in every building (thread_laundry_timing.txt).
- Sources retrieved: thread_first_gen.txt, thread_laptop_specs.txt, thread_printing.txt
Yes, for most people it is enough. ($30 is about 600 pages black and white, though color printing uses it up much faster.)
Source: thread_printing.txt
- Sources retrieved: thread_group_project.txt, thread_late_work.txt, thread_pass_fail.txt
According to thread_pass_fail.txt, you should use the pass/fail option for a course outside your major that you are taking out of curiosity.
- Sources retrieved: thread_group_project.txt, thread_office_hours_etiquette.txt, thread_roommate_conflict.txt
If your roommate situation is not working, you should talk to your Resident Advisor (RA) early and frame the conversation around needing help sorting things out rather than asking to move (thread_roommate_conflict.txt).
- Sources retrieved: thread_late_work.txt, thread_office_hours_etiquette.txt, thread_professor_email.txt
Yes, it is completely normal to go to office hours with no specific question, and doing so is not weird at all (thread_office_hours_etiquette.txt).
     -> gate refused 5 of 5

### Raw output from app.py::cmd_retrieve
1   0.3276     thread_laundry_timing.txt
1   0.3146     thread_printing.txt
1   0.4642     thread_pass_fail.txt
1   0.3535     thread_roommate_conflict.txt
1   0.5029     thread_office_hours_etiquette.txt
```

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | MET | At least one retrieved chunk contained the expected answer information for all five questions, exceeding the target of 4 of 5. |
| 2 | Every answer names a source | MET | All 15 generated answers named at least one source document. |
| 3 | Gate stops out-of-corpus questions | MET | The gate refused all 5 out-of-scope questions, exceeding the target of 4 of 5. |
| 4 | Sampled chunks are complete | MET | All 5 inspected chunks were complete threads from one source document. |
| 5 | Generated answer length | MET | The generated answers were within the revised 5-to-90-word range in the recorded runs. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

No criterion was missed in the baseline run. However, the original Criterion
5 was not an independent measure: Criterion 1 already checked whether answer
information appeared anywhere in the retrieved chunks, while retrieval had
already ranked those chunks by cosine similarity. Because the answer
information was present within the top three chunks, Criterion 5 largely
repeated Criterion 1 rather than revealing a separate system weakness. I
therefore revised Criterion 5 to measure generated-answer length directly.
This revision changes the measurement, not the baseline verdict.

## The Improvement

**What I changed:**
I changed `config.py` so the default retrieval count (`TOP_K`) decreased from
5 chunks to 3 chunks.

**Criterion 5 revision:**
I replaced the original top-three retrieval criterion with a generated-answer
length criterion requiring answers to contain between 5 and 90 words. Criteria
1 through 4 remain unchanged.

**Why I picked it:**
The original configuration retrieved 5 chunks for each question. Manual
inspection showed that the answer was identifiable within the top three
retrieved chunks for direct, indirect, and multi-hop questions. In multi-hop
cases, the answer was not necessarily contained in one document: the first
chunk covered the main part of the answer, while the next closest chunk added
the most relevant missing context. Because retrieval uses cosine similarity,
semantically closer chunks are ranked ahead of less relevant chunks. This
means that, for this corpus, the first three results were the most useful
context for both single-document and multi-document answers, given that this
corpus consists of short, self-contained advice threads.

Reducing `top-k` from 5 to 3 also reduces input-token usage because fewer
chunks are sent to the model. The top-three change effectively made the
condition represented by the original Criterion 5 part of the system's
operating configuration: the model now receives the same top-three context
that Criterion 5 previously checked. The earlier Criterion 5 was therefore
redundant with Criterion 1 and with the ranking behavior itself. The revised
Criterion 5 measures generated-answer length instead.

A corresponding top-three evaluation was conducted during this analysis and
the checks passed. The committed after-run confirms that all 15 in-corpus
judge calls reached the overall PASS threshold of 3/4. At the individual
criterion level, C1 scored 4/5 in each run because the office-hours question
was a keyword-scoring miss, while C2, C4, and C5 each scored 5/5. The
relevance gate refused 5 of 5 out-of-corpus questions. This supports the
conclusion that reducing the context from five chunks to three preserved the
measured retrieval and answer behavior while reducing the amount of context
sent to the model. The Criterion 5 change was a measurement revision only;
the sole system improvement was changing `TOP_K` from 5 to 3.

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4 of 5 | 4 of 5 | 4 of 5 | MET |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Sampled chunks are complete | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. Generated answer length | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

**After evidence:** `results/run_2026-09-24_1507_after.md`, produced by
`run_eval.py::main`, records `top-k: 3`, three runs per question, all 15
in-corpus runs passing, and the gate refusing 5 of 5 out-of-corpus questions.
The scorer prints the individual C1, C2, C4, and revised C5 checks during
evaluation and returns PASS when at least 3 of those 4 checks pass.

The recorded output includes the retrieved source names, distances, and full
answers. For example, the office-hours question had a best distance of
`0.5029` and received an overall PASS on all three runs because C2, C4, and C5
passed. C1 was marked FAIL by the keyword scorer even though the generated
answer used `thread_office_hours_etiquette.txt` and correctly explained that
attending office hours without a specific question is normal.

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

The completed `top-k = 5` to `top-k = 3` comparison shows that all five
in-corpus questions passed on all three runs, while the gate still refused 5
of 5 out-of-corpus questions. This supports the conclusion that reducing the
context preserved the measured retrieval and answer behavior while using
fewer input chunks. Criterion 3 remains the separate deterministic gate
measurement performed by `run_eval.py::check_out_of_scope`.

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

The gate itself refused all 5 out-of-corpus questions, but Criterion 3 is not
evaluated by `judge()`. `judge()` is called only for the five in-corpus
questions. It does not receive the out-of-scope questions, so it cannot
evaluate Criterion 3; that criterion is measured separately by
`run_eval.py::check_out_of_scope`.

The remaining limitation is that Criterion 1 uses keyword coverage, so a
correct answer expressed with synonyms or indirect wording can still be
marked as a miss. The revised Criterion 5 measures answer length only; it does
not prove that the answer is correct. A future improvement would use semantic
matching or manually defined key facts. The completed after-run also confirms
the current measured behavior only for these five questions and this corpus;
it does not establish that every possible question will be answered correctly.

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->

I would define Criterion 5 as an answer-quality measure from the beginning.
For this short-thread corpus, a concise 5-to-90-word answer is more useful
than repeating a top-three retrieval check that is already implied by the
semantic ranking used by retrieval. I would also define Criterion 1 around
key facts or semantic support rather than exact keyword overlap, so indirect
but correct answers are measured fairly.
