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
| 1 | Retrieved chunks contain the answer | MET | The answer-containing source was ranked first for all five questions, so the target of at least 4 of 5 was exceeded. |
| 2 | Every answer names a source | MET | All 15 generated answers named at least one source document. |
| 3 | Gate stops out-of-corpus questions | MET | The gate refused all 5 out-of-scope questions, exceeding the target of 4 of 5. |
| 4 | Sampled chunks are complete | MET | All 5 inspected chunks were complete threads from one source document. |
| 5 | Answer chunk is in first three results | MET | The answer-containing source ranked first for all five questions. |

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

No criterion was missed in the baseline run. Because every answer-containing
chunk ranked first, Criterion 5 was not a demanding test of ranking quality.
I would tighten that target in a future project to require the answer-containing
chunk to appear first for all 5 questions, rather than allowing the first 3
results.

## The Improvement

**What I changed:**
I will reduce the default retrieval count from 3 chunks to 2 chunks.

**Why I picked it:**
All five answer-containing chunks ranked first with `top-k = 3`, so the third
chunk was not needed to find the answer. Reducing `top-k` tests whether the
system can preserve retrieval quality while sending less unrelated context to
the model.

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Sampled chunks are complete | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. Answer chunk is in first three results | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

**After evidence:** `results/run_2026-09-21_0253_after.md`, produced by
`run_eval.py::main`, recorded `top-k: 2` and three runs per question. The
answer-containing source remained in the retrieved results for all five
questions, every answer named a source, and the gate refused 5 of 5
out-of-corpus questions.

```text
top-k: 2 · relevance cutoff: 0.6
     -> gate refused 5 of 5
- Sources retrieved: thread_commuting.txt, thread_laundry_timing.txt
Laundry is actually free in the dorms on Tuesday and Wednesday mornings in every building (thread_laundry_timing.txt).
- Sources retrieved: thread_laptop_specs.txt, thread_printing.txt
Yes, for most people the printing quota of $30 is enough.
Source: thread_printing.txt
- Sources retrieved: thread_late_work.txt, thread_pass_fail.txt
You should use the pass/fail option for a course outside your major that you are taking because you are curious.
Source: thread_pass_fail.txt
- Sources retrieved: thread_group_project.txt, thread_roommate_conflict.txt
If your roommate situation is not working, you should talk to your RA early and frame it as needing help sorting things out rather than asking to move (thread_roommate_conflict.txt).
- Sources retrieved: thread_office_hours_etiquette.txt, thread_professor_email.txt
Yes, it is not weird to go to office hours with no specific question, and it is considered a normal thing to do (thread_office_hours_etiquette.txt).
```

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

Yes. With `top-k = 2`, all five questions still retrieved the chunk containing
the answer, all generated answers named a source, and the gate still refused
5 of 5 out-of-corpus questions. The run used 6,994 total tokens compared with
9,298 for the `top-k = 3` baseline, although the exact generated wording also
varied between runs.

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

No criteria remained missed after the improvement. The main remaining
limitation is that some answers omit secondary details even when the retrieved
chunk contains them; for example, the printing answer sometimes omitted the
600-page figure. I stopped because the five stated targets were still met, but
answer completeness would be the next issue to improve.

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->

I would make Criterion 5 stricter: the answer-containing chunk must rank first
for all 5 test questions. The baseline already showed that all five ranked
first, so this would measure ranking quality more precisely than allowing any
of the first three results.
