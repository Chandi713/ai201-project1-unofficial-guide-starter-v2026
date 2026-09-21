# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
<!-- e.g. "One of my questions is about a topic only two documents mention, so
     I expect that one to be hard." -->
I chose 4 of 5 test questions to include answer because almost all have related document in the advice_threads corpus and so the top-5 retrieval usually includes the required information. Allowing 1 miss is purposely set as there might be an answer split across chunks or answered in an indirect manner which might not have wordings that could be caught by similarity or kew-word comparisions.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
<!-- Why all five and not four? What about your setup makes that achievable —
     or what would have to go wrong for it not to be? -->
I chose 5 out of 5 because every retrieved chunk includes its source documents, and the generation step is designed to cite that source in answer.The failure could occur only if the checkpoint allows a question through without useful retrived result or model omits the source.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**
<!-- What did your distances look like when you set the cutoff in Milestone 4?
     Was there a clean gap, or did the two groups overlap? -->

I chose at least 4 of 5 because the out-of-scope questions had distances
between 0.78 and 0.93, all above the 0.6 cutoff, so the gate appears to distinguish them from my actual corpus. On miss could possibly be found if a question has a semantic resemblance with the corpus key words but at the same time has nothing to do with the queries answered within our corpus.

---

## 4. Something about your chunks

<!-- YOU WRITE THIS ONE.

     How would you know if your chunks were the right size? Name something
     countable or observable.

     Examples of the right shape — don't copy these, they should come from
     what you actually saw in Milestone 3:
       - "At least 4 of 5 sampled chunks read as a complete thought, with no
          sentence cut in half at either end."
       - "No chunk is shorter than 200 characters, since anything below that
          in my corpus turned out to be a heading with no content under it." -->
At least 4 of 5 sampled chunks must contain all the information about the thread without splitting it into different chunks or combining the content with the separate document. 


**Why this target:**
The advice-thread corpus contains short, self-contained documents and the 800 character chunk preserve the whole thread/discussion without cutting-down the information or getting intermingled with a different document/thread. There could be a possible exception of a document crossing the chunk boundary, but a tiny exceptional document does not mean that we should increase the chunk-size to involve it. It is so because if we increase the chunk-size, then in case of a large chunk, the query might retrieve less precise chunk or it might exceed model's context reducing the answer quality.



---

## 5. Your choice

<!-- YOU WRITE THIS ONE TOO.

     Pick something you actually care about getting right. It could be about
     speed, about refusals, about a particular kind of question your corpus
     handles badly, about source attribution being correct rather than merely
     present — anything, as long as it names a number or an observable
     outcome. -->
For at least 4 of my 5 test questions, the answer-containing chunk appears
within the first 3 retrieved results.


**Why this target:**
I chose the first three results because my corpus contains no more than three
documents with closely interconnected topics for a given question. Since most
chunks in my corpus correspond to one complete document, these three chunks
should provide enough relevant information to answer the question. Limiting
the useful results to the first three also reduces the amount of unrelated text
sent to the model, thus reducing the input tokens.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
