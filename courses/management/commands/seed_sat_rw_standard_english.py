"""
Seed data: 'SAT Reading & Writing: Standard English Conventions' -- a deep-dive
course covering the Standard English Conventions domain of the digital SAT
Reading and Writing section (approximately 26% of the section).

Topics covered:
  - Sentence Boundaries (fragments, run-ons, fused sentences)
  - Subject-Verb Agreement
  - Pronoun Agreement and Case
  - Modifiers (misplaced and dangling)
  - Parallel Structure
  - Punctuation: Commas, Semicolons, Colons, and Dashes
  - Verb Tense and Consistency

Run:
    python manage.py seed_sat_rw_standard_english
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "SAT Reading & Writing: Standard English Conventions",
    "slug": "sat-rw-standard-english",
    "program": "SAT",
    "subject": "rla",
    "description": (
        "A focused deep-dive into the SAT Standard English Conventions domain, covering the "
        "grammar and punctuation rules tested on every digital SAT. Seven targeted lessons "
        "address sentence boundaries, subject-verb agreement, pronoun case, modifiers, parallel "
        "structure, punctuation marks, and verb tense. Thirty realistic practice questions with "
        "full rule-based explanations build the precision needed to answer every Standard English "
        "Conventions question correctly on test day."
    ),
    "lessons": [
        (
            "1. Sentence Boundaries",
            "**Sentence Boundaries** questions test whether you can recognize a complete sentence "
            "and fix structures that are broken or improperly joined. Every complete sentence "
            "requires three things: a **subject** (who or what the sentence is about), a "
            "**verb** (the action or state), and a **complete thought** (the sentence can stand "
            "alone and makes sense by itself).\n\n"
            "**Fragments** are incomplete sentences. They are missing a subject, a verb, or a "
            "complete thought.\n"
            "- Fragment (missing verb): \"The scientist working late in the lab.\"\n"
            "- Complete: \"The scientist was working late in the lab.\"\n\n"
            "**Run-on sentences** and **fused sentences** occur when two independent clauses are "
            "joined incorrectly. A fused sentence has no punctuation at all between the clauses; "
            "a comma splice uses only a comma, which is not strong enough to join two independent "
            "clauses.\n"
            "- Fused: \"She finished the exam she felt relieved.\"\n"
            "- Comma splice: \"She finished the exam, she felt relieved.\"\n\n"
            "**Three correct fixes** for run-ons:\n"
            "- **Period**: separate them into two sentences.\n"
            "- **Semicolon**: join them with a semicolon if they are closely related.\n"
            "- **Comma + coordinating conjunction (FANBOYS)**: for, and, nor, but, or, yet, so.\n\n"
            "Before/After examples:\n"
            "- Incorrect: \"The river flooded its banks, emergency crews were deployed immediately.\"\n"
            "- Correct: \"The river flooded its banks; emergency crews were deployed immediately.\"\n\n"
            "- Incorrect: \"Running through the park every morning. He felt energized.\"\n"
            "- Correct: \"Running through the park every morning, he felt energized.\"\n\n"
            "⚠️ Common mistake: treating a long fragment as a sentence just because it sounds "
            "complete. Always check for both a subject and a finite verb.\n\n"
            "💡 Tip: on the SAT, if a sentence starts with a verb ending in -ing and has no "
            "subject before it, it is almost always a fragment or a dangling modifier -- look for "
            "a fix that attaches it to the main clause."
        ),
        (
            "2. Subject-Verb Agreement",
            "**Subject-Verb Agreement** requires that a singular subject takes a singular verb "
            "and a plural subject takes a plural verb. This sounds simple, but the SAT deliberately "
            "places distractors between the subject and the verb to obscure the relationship.\n\n"
            "**The core rule:**\n"
            "- Singular: \"The dog runs in the yard.\"\n"
            "- Plural: \"The dogs run in the yard.\"\n\n"
            "**Tricky case 1 -- Prepositional phrases:** A prepositional phrase between the "
            "subject and verb does not change the subject's number.\n"
            "- Incorrect: \"The box of apples are on the counter.\"\n"
            "- Correct: \"The box of apples is on the counter.\" (Subject = box, singular)\n\n"
            "**Tricky case 2 -- Collective nouns:** Words like team, committee, class, family, "
            "and government are usually treated as singular in American English.\n"
            "- \"The committee has reached its decision.\"\n\n"
            "**Tricky case 3 -- Indefinite pronouns:** The pronouns each, every, either, neither, "
            "one, everyone, everybody, someone, and anyone are always **singular**.\n"
            "- \"Each of the students is responsible for their own work.\"\n\n"
            "**Tricky case 4 -- Compound subjects with or/nor:** The verb agrees with the subject "
            "closest to it.\n"
            "- \"Neither the manager nor the employees were informed.\"\n"
            "- \"Neither the employees nor the manager was informed.\"\n\n"
            "Before/After examples:\n"
            "- Incorrect: \"The impact of the new policies are still being studied.\"\n"
            "- Correct: \"The impact of the new policies is still being studied.\"\n\n"
            "⚠️ Common mistake: agreeing the verb with a noun in a prepositional phrase rather "
            "than with the true subject.\n\n"
            "💡 Tip: cross out any prepositional phrases between the subject and verb before "
            "checking agreement. This instantly reveals the true subject."
        ),
        (
            "3. Pronoun Agreement and Case",
            "**Pronoun Agreement** requires that a pronoun match its **antecedent** -- the noun "
            "it refers to -- in both number (singular/plural) and gender. **Pronoun Case** "
            "requires using the correct form of the pronoun depending on its role in the sentence "
            "(subject, object, or possessive).\n\n"
            "**Agreement rules:**\n"
            "- Singular antecedent: use singular pronoun (he, she, it, his, her, its).\n"
            "- Plural antecedent: use plural pronoun (they, them, their).\n"
            "- Incorrect: \"Every student must submit their essay by Friday.\" "
            "(Every = singular; the formally agreed form in edited prose is \"his or her\".)\n\n"
            "**Ambiguous reference:** A pronoun is ambiguous when it could refer to more than "
            "one antecedent.\n"
            "- Ambiguous: \"When Maria told Sofia the news, she burst into tears.\"\n"
            "- Clear: \"When Maria told Sofia the news, Sofia burst into tears.\"\n\n"
            "**Who vs. Whom:**\n"
            "- Use **who** when the pronoun is a subject (replace with he/she).\n"
            "- Use **whom** when the pronoun is an object (replace with him/her).\n"
            "- \"She is the scientist who discovered the compound.\" (who = she, subject)\n"
            "- \"He is the scientist whom the committee honored.\" (whom = him, object)\n\n"
            "**Subject vs. Object pronouns:**\n"
            "- Subject: I, he, she, we, they\n"
            "- Object: me, him, her, us, them\n\n"
            "Before/After examples:\n"
            "- Incorrect: \"Between you and I, the project is behind schedule.\"\n"
            "- Correct: \"Between you and me, the project is behind schedule.\"\n\n"
            "⚠️ Common mistake: using \"I\" after a preposition because it sounds formal. "
            "Prepositions always take object pronouns: with me, between us, for him.\n\n"
            "💡 Tip: to test who vs. whom, substitute he or him. If he works, use who; "
            "if him works, use whom."
        ),
        (
            "4. Modifiers",
            "**Modifiers** are words, phrases, or clauses that describe or qualify other words in "
            "a sentence. The SAT tests two major modifier errors: **misplaced modifiers** (the "
            "modifier is not close enough to the word it describes) and **dangling modifiers** "
            "(the word being modified is not in the sentence at all).\n\n"
            "**Adjectives vs. Adverbs:**\n"
            "- **Adjectives** modify nouns and pronouns (tall building, careful plan).\n"
            "- **Adverbs** modify verbs, adjectives, and other adverbs (ran quickly, extremely "
            "tall, very carefully).\n"
            "- Incorrect: \"She performed incredible on the exam.\"\n"
            "- Correct: \"She performed incredibly on the exam.\" (modifies the verb 'performed')\n\n"
            "**Misplaced modifiers:** The modifier is placed too far from the word it modifies, "
            "creating an unintended or absurd meaning.\n"
            "- Misplaced: \"The researcher observed the cells using a microscope with blue eyes.\"\n"
            "- Correct: \"Using a microscope, the researcher with blue eyes observed the cells.\"\n\n"
            "**Dangling modifiers:** An introductory phrase implies a subject that is not the "
            "actual subject of the main clause.\n"
            "- Dangling: \"Having studied for hours, the exam seemed easy.\"\n"
            "(The exam did not study -- the student did.)\n"
            "- Correct: \"Having studied for hours, she found the exam easy.\"\n\n"
            "Before/After examples:\n"
            "- Incorrect: \"Walking to the station, the rain began to fall.\"\n"
            "- Correct: \"Walking to the station, I was caught in the rain.\"\n\n"
            "⚠️ Common mistake: leaving a dangling participial phrase at the start of a sentence "
            "without ensuring the main clause subject is the one performing the action.\n\n"
            "💡 Tip: whenever an SAT sentence begins with a verb + -ing or verb + -ed phrase "
            "followed by a comma, ask yourself: who is doing that action? That person or thing "
            "must be the subject immediately after the comma."
        ),
        (
            "5. Parallel Structure",
            "**Parallel Structure** (also called parallelism) requires that items in a series, "
            "list, or comparison share the same grammatical form. When the SAT presents a "
            "sentence with a list of activities, qualities, or ideas, all items must be expressed "
            "as the same part of speech or the same verb form.\n\n"
            "**The core rule:**\n"
            "- Incorrect: \"She likes hiking, to swim, and to run.\"\n"
            "- Correct: \"She likes hiking, swimming, and running.\" (all gerunds)\n"
            "- Also correct: \"She likes to hike, to swim, and to run.\" (all infinitives)\n\n"
            "**Parallelism with correlative conjunctions:**\n"
            "Correlative conjunctions come in pairs and require identical grammatical structures "
            "on both sides.\n"
            "- not only...but also\n"
            "- either...or\n"
            "- both...and\n"
            "- neither...nor\n"
            "- Incorrect: \"The study was not only thorough but also it was convincing.\"\n"
            "- Correct: \"The study was not only thorough but also convincing.\" (both adjectives)\n\n"
            "**Parallel comparisons:** When comparing two things, use the same grammatical "
            "structure on both sides of the comparison.\n"
            "- Incorrect: \"The cost of renting is higher than to buy.\"\n"
            "- Correct: \"The cost of renting is higher than the cost of buying.\"\n\n"
            "Before/After examples:\n"
            "- Incorrect: \"The committee agreed to review the evidence, holding new hearings, "
            "and a final report would be issued.\"\n"
            "- Correct: \"The committee agreed to review the evidence, hold new hearings, "
            "and issue a final report.\"\n\n"
            "⚠️ Common mistake: mixing gerunds and infinitives in the same list without noticing "
            "the shift in form.\n\n"
            "💡 Tip: underline each item in the series and label its part of speech. If the "
            "labels are different, the sentence lacks parallelism."
        ),
        (
            "6. Punctuation: Commas, Semicolons, Colons, and Dashes",
            "**Punctuation** questions on the SAT focus on whether a punctuation mark correctly "
            "reflects the grammatical relationship between the parts of a sentence. The four "
            "marks tested most heavily are the comma, semicolon, colon, and em dash.\n\n"
            "**Comma rules:**\n"
            "- Use a comma + coordinating conjunction (FANBOYS) to join two independent clauses.\n"
            "- Use commas to set off nonessential (parenthetical) information.\n"
            "- Use commas in a list of three or more items.\n"
            "- **Comma splice**: using only a comma to join two independent clauses is wrong.\n"
            "  - Incorrect: \"The experiment failed, the team revised their hypothesis.\"\n"
            "  - Correct: \"The experiment failed, so the team revised their hypothesis.\"\n\n"
            "**Semicolons** join two closely related independent clauses without a conjunction.\n"
            "- Correct: \"The experiment failed; the team revised their hypothesis.\"\n"
            "- A semicolon cannot join a dependent clause to an independent clause.\n\n"
            "**Colons** introduce a list, explanation, or elaboration. The clause before the "
            "colon must be a complete independent clause.\n"
            "- Correct: \"She brought three things to the lab: a notebook, a pen, and a ruler.\"\n"
            "- Incorrect: \"She brought: a notebook, a pen, and a ruler.\"\n\n"
            "**Em dashes** add emphasis or set off a parenthetical element. They can replace "
            "commas, parentheses, or a colon.\n"
            "- \"The answer -- surprising to everyone -- was published the next morning.\"\n\n"
            "Before/After examples:\n"
            "- Incorrect: \"The new policy has one clear goal, to reduce carbon emissions.\"\n"
            "- Correct: \"The new policy has one clear goal: to reduce carbon emissions.\"\n\n"
            "⚠️ Common mistake: placing a colon after a verb or preposition. The word before a "
            "colon must complete a full independent clause.\n\n"
            "💡 Tip: if two independent clauses are separated by only a comma with no conjunction, "
            "it is always a comma splice -- replace the comma with a semicolon, add a FANBOYS "
            "conjunction, or split into two sentences."
        ),
        (
            "7. Verb Tense and Consistency",
            "**Verb Tense** questions ask you to choose the tense that correctly reflects when an "
            "action takes place relative to other events in the passage. **Tense Consistency** "
            "questions ask you to keep the tense the same throughout a sentence or passage unless "
            "there is a logical reason to shift.\n\n"
            "**The main tenses:**\n"
            "- **Simple**: past (wrote), present (writes), future (will write)\n"
            "- **Perfect**: past perfect (had written), present perfect (has written), "
            "future perfect (will have written)\n"
            "- **Progressive**: past progressive (was writing), present progressive (is writing)\n\n"
            "**When to use the perfect tense:**\n"
            "- Use **past perfect** (had + past participle) for an action completed before "
            "another past action: \"By the time she arrived, the panel had already adjourned.\"\n"
            "- Use **present perfect** (has/have + past participle) for an action that began in "
            "the past and continues or is relevant now: \"Scientists have discovered three new "
            "species this year.\"\n\n"
            "**Tense consistency:** Do not switch tenses mid-sentence or mid-paragraph without "
            "a logical reason.\n"
            "- Incorrect: \"The author introduces the argument and then provided evidence.\"\n"
            "- Correct: \"The author introduces the argument and then provides evidence.\"\n\n"
            "**Subjunctive mood:** Use the subjunctive for hypothetical, contrary-to-fact, or "
            "wished-for situations. The key form is 'were' instead of 'was'.\n"
            "- Correct: \"If I were the director, I would expand the program.\"\n"
            "- Incorrect: \"If I was the director, I would expand the program.\"\n\n"
            "Before/After examples:\n"
            "- Incorrect: \"She studies all night and then fell asleep at her desk.\"\n"
            "- Correct: \"She studied all night and then fell asleep at her desk.\"\n\n"
            "⚠️ Common mistake: switching from present to past tense in a single narrative "
            "without a time signal, especially when summarizing a text.\n\n"
            "💡 Tip: when the SAT asks about verb tense, look for time-signal words in the "
            "surrounding sentences (yesterday, by the time, since, already, next year) -- these "
            "clues tell you which tense is required."
        ),
    ],
    "mcqs": [
        # --- Lesson 1: Sentence Boundaries (4 questions) ---
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The lead researcher presented her findings at the conference. ______ a standing "
                "ovation from the audience.\n\n"
                "(A) Receiving\n"
                "(B) She received\n"
                "(C) To receive\n"
                "(D) Having received"
            ),
            "difficulty": 1,
            "choices": [
                ("(A) Receiving", False),
                ("(B) She received", True),
                ("(C) To receive", False),
                ("(D) Having received", False),
            ],
            "explanation": (
                "The blank must begin a complete, independent sentence. Choice (B) 'She received' "
                "provides a subject (She) and a finite verb (received), creating a complete sentence. "
                "Choices (A), (C), and (D) all produce fragments because they lack a proper subject "
                "and finite verb combination that can stand alone as an independent clause."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The ancient temple had stood for centuries ______ a powerful earthquake reduced "
                "it to rubble in a matter of minutes.\n\n"
                "(A) , but\n"
                "(B) , so\n"
                "(C) and\n"
                "(D) ,"
            ),
            "difficulty": 1,
            "choices": [
                ("(A) , but", True),
                ("(B) , so", False),
                ("(C) and", False),
                ("(D) ,", False),
            ],
            "explanation": (
                "Two independent clauses -- 'The ancient temple had stood for centuries' and 'a "
                "powerful earthquake reduced it to rubble' -- must be joined correctly. Choice (A) "
                "uses a comma + the coordinating conjunction 'but', which correctly joins two "
                "independent clauses and reflects the contrasting relationship. Choice (D) creates "
                "a comma splice. Choice (C) lacks the necessary comma before a coordinating "
                "conjunction joining independent clauses. Choice (B) uses 'so', which implies the "
                "first clause caused the second, which is illogical here."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "Many students struggle with calculus ______ they rarely practice solving problems "
                "without a calculator.\n\n"
                "(A) , because\n"
                "(B) because\n"
                "(C) ; because\n"
                "(D) : because"
            ),
            "difficulty": 2,
            "choices": [
                ("(A) , because", False),
                ("(B) because", True),
                ("(C) ; because", False),
                ("(D) : because", False),
            ],
            "explanation": (
                "The word 'because' is a subordinating conjunction that introduces a dependent "
                "clause. When a dependent clause follows an independent clause, no comma is needed. "
                "Choice (B) is correct. Choice (A) incorrectly places a comma before a dependent "
                "clause. Choice (C) is wrong because a semicolon must be followed by an independent "
                "clause, not a dependent clause beginning with 'because'. Choice (D) misuses a colon, "
                "which introduces a list or explanation, not a causal clause."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "Established in 1905, the library ______ one of the oldest in the region, "
                "attracting scholars and researchers from around the world.\n\n"
                "(A) it is\n"
                "(B) being\n"
                "(C) is\n"
                "(D) which is"
            ),
            "difficulty": 3,
            "choices": [
                ("(A) it is", False),
                ("(B) being", False),
                ("(C) is", True),
                ("(D) which is", False),
            ],
            "explanation": (
                "The sentence needs a finite verb to make the main clause complete. Choice (C) 'is' "
                "provides the necessary verb, making 'the library is one of the oldest in the region' "
                "a complete independent clause. Choice (A) 'it is' creates a run-on because 'it' "
                "would be a redundant second subject. Choice (B) 'being' is a participle, not a "
                "finite verb, so it would leave the sentence without a main verb. Choice (D) 'which "
                "is' creates a relative clause that cannot stand alone."
            ),
        },
        # --- Lesson 2: Subject-Verb Agreement (4 questions) ---
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The collection of rare manuscripts ______ stored in a climate-controlled vault "
                "at the university.\n\n"
                "(A) are\n"
                "(B) were\n"
                "(C) is\n"
                "(D) have been"
            ),
            "difficulty": 1,
            "choices": [
                ("(A) are", False),
                ("(B) were", False),
                ("(C) is", True),
                ("(D) have been", False),
            ],
            "explanation": (
                "The subject is 'collection', a singular noun. The prepositional phrase 'of rare "
                "manuscripts' modifies the subject but does not change its number. A singular subject "
                "requires a singular verb. Choice (C) 'is' is correct. Choices (A) 'are' and (B) "
                "'were' are plural verbs that incorrectly agree with the noun in the prepositional "
                "phrase. Choice (D) 'have been' is also plural."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "Either the project manager or the team members ______ responsible for submitting "
                "the final report by Friday.\n\n"
                "(A) is\n"
                "(B) are\n"
                "(C) was\n"
                "(D) has been"
            ),
            "difficulty": 2,
            "choices": [
                ("(A) is", False),
                ("(B) are", True),
                ("(C) was", False),
                ("(D) has been", False),
            ],
            "explanation": (
                "With compound subjects joined by 'either...or', the verb agrees with the subject "
                "closest to it. The subject closest to the verb is 'the team members', which is "
                "plural. Therefore, the verb must be plural. Choice (B) 'are' is correct. Choice (A) "
                "'is' would be correct if the singular subject 'the project manager' were closest to "
                "the verb, but it is not. Choices (C) and (D) use incorrect tense."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "Each of the proposals submitted by the research teams ______ been reviewed by "
                "an independent panel.\n\n"
                "(A) have\n"
                "(B) has\n"
                "(C) were\n"
                "(D) are"
            ),
            "difficulty": 2,
            "choices": [
                ("(A) have", False),
                ("(B) has", True),
                ("(C) were", False),
                ("(D) are", False),
            ],
            "explanation": (
                "The subject is 'Each', an indefinite pronoun that is always singular. 'Each of the "
                "proposals' means every single proposal considered individually. Singular subjects "
                "take singular verbs. Choice (B) 'has' is the correct singular present perfect form. "
                "Choice (A) 'have' is plural. Choices (C) and (D) are incorrect in both number and "
                "form for this context."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The committee, despite the objections raised by several prominent members, "
                "______ voted to proceed with the construction project.\n\n"
                "(A) have\n"
                "(B) were\n"
                "(C) has\n"
                "(D) are"
            ),
            "difficulty": 3,
            "choices": [
                ("(A) have", False),
                ("(B) were", False),
                ("(C) has", True),
                ("(D) are", False),
            ],
            "explanation": (
                "The subject is 'committee', a collective noun that is treated as singular in "
                "American English. The long parenthetical phrase 'despite the objections raised by "
                "several prominent members' is set off by commas and does not change the subject. "
                "Choice (C) 'has' is the correct singular present perfect verb. Choices (A) 'have' "
                "and (D) 'are' are plural. Choice (B) 'were' is plural and past tense."
            ),
        },
        # --- Lesson 3: Pronoun Agreement and Case (4 questions) ---
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The award was given to ______ the review committee deemed the most innovative "
                "researcher of the year.\n\n"
                "(A) whoever\n"
                "(B) whomever\n"
                "(C) who\n"
                "(D) whom"
            ),
            "difficulty": 2,
            "choices": [
                ("(A) whoever", False),
                ("(B) whomever", True),
                ("(C) who", False),
                ("(D) whom", False),
            ],
            "explanation": (
                "The pronoun is the object of the preposition 'to', so an object form is required. "
                "Within the clause 'the review committee deemed ___ the most innovative researcher', "
                "the pronoun is the direct object of 'deemed' -- substitute 'him' (object) to "
                "confirm: 'the committee deemed him'. Since 'him' works, use the object form. "
                "Because the entire clause functions as the object of 'to', the correct choice is "
                "'whomever' (B). 'Whoever' and 'who' are subject forms and are incorrect here."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The professors disagreed about the interpretation; Dr. Chen believed the text "
                "was satirical, while ______ saw it as straightforwardly sincere.\n\n"
                "(A) her colleague Dr. Reyes\n"
                "(B) they\n"
                "(C) it\n"
                "(D) him"
            ),
            "difficulty": 1,
            "choices": [
                ("(A) her colleague Dr. Reyes", True),
                ("(B) they", False),
                ("(C) it", False),
                ("(D) him", False),
            ],
            "explanation": (
                "The original sentence has an ambiguous pronoun problem. 'Her' or 'they' could "
                "refer to either professor, making the meaning unclear. Choice (A) resolves the "
                "ambiguity by naming the second professor directly ('Dr. Reyes') and clarifying "
                "the relationship ('her colleague'). Choice (B) 'they' is plural and introduces "
                "a number disagreement. Choice (C) 'it' refers to a thing, not a person. Choice "
                "(D) 'him' introduces an unspecified male pronoun with no clear antecedent."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The biology department awarded the fellowship to my lab partner and ______.\n\n"
                "(A) I\n"
                "(B) myself\n"
                "(C) me\n"
                "(D) we"
            ),
            "difficulty": 1,
            "choices": [
                ("(A) I", False),
                ("(B) myself", False),
                ("(C) me", True),
                ("(D) we", False),
            ],
            "explanation": (
                "The pronoun follows the preposition 'to', so it must be in the object case. "
                "Removing 'my lab partner and' makes this clear: 'awarded the fellowship to me' -- "
                "not 'to I' or 'to myself'. Choice (C) 'me' is the correct object-case pronoun. "
                "Choice (A) 'I' is a subject pronoun and cannot follow a preposition. Choice (B) "
                "'myself' is a reflexive/emphatic pronoun and should not be used as a simple object. "
                "Choice (D) 'we' is also a subject pronoun."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The novelist, along with three editors, revised ______ manuscript over the course "
                "of six months.\n\n"
                "(A) their\n"
                "(B) its\n"
                "(C) her\n"
                "(D) our"
            ),
            "difficulty": 3,
            "choices": [
                ("(A) their", False),
                ("(B) its", False),
                ("(C) her", True),
                ("(D) our", False),
            ],
            "explanation": (
                "The antecedent for the possessive pronoun is 'the novelist', which is singular and "
                "refers to a specific individual author. The phrase 'along with three editors' is a "
                "parenthetical modifier and does not change the singular subject. The context "
                "indicates the novelist is female. Choice (C) 'her' correctly agrees with the "
                "singular antecedent. Choice (A) 'their' is plural. Choice (B) 'its' refers to "
                "non-persons. Choice (D) 'our' implies the speaker is included."
            ),
        },
        # --- Lesson 4: Modifiers (4 questions) ---
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "______ the data carefully, the team identified a significant flaw in the "
                "original methodology.\n\n"
                "(A) After analyzing\n"
                "(B) The data was analyzed and\n"
                "(C) Having been analyzed\n"
                "(D) When the analysis of"
            ),
            "difficulty": 1,
            "choices": [
                ("(A) After analyzing", True),
                ("(B) The data was analyzed and", False),
                ("(C) Having been analyzed", False),
                ("(D) When the analysis of", False),
            ],
            "explanation": (
                "An introductory participial phrase must refer to the subject of the main clause. "
                "The main clause subject is 'the team', and the team performed the analysis. Choice "
                "(A) 'After analyzing the data carefully, the team...' correctly places the doer "
                "(the team) as the subject. Choice (C) 'Having been analyzed' is passive and implies "
                "the team was analyzed. Choice (B) changes the structure entirely, and Choice (D) "
                "creates a dangling modifier because 'the analysis' did not identify the flaw."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The professor only teaches graduate students ______ in the spring semester.\n\n"
                "(A) which is offered\n"
                "(B) who are enrolled\n"
                "(C) a class\n"
                "(D) during the time"
            ),
            "difficulty": 2,
            "choices": [
                ("(A) which is offered", False),
                ("(B) who are enrolled", True),
                ("(C) a class", False),
                ("(D) during the time", False),
            ],
            "explanation": (
                "The sentence requires a modifier that logically describes 'graduate students'. "
                "Choice (B) 'who are enrolled in the spring semester' is a relative clause that "
                "correctly modifies 'graduate students' and clarifies which students the professor "
                "teaches. Choice (A) 'which is offered' would need to modify a course or class, "
                "not students. Choice (C) adds an object but does not form a logical or grammatical "
                "modifier. Choice (D) creates an awkward and incomplete phrase."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "______ in a remote mountain village, the painter's early experiences "
                "profoundly shaped her artistic vision.\n\n"
                "(A) She grew up\n"
                "(B) Growing up\n"
                "(C) To grow up\n"
                "(D) She had grown up"
            ),
            "difficulty": 2,
            "choices": [
                ("(A) She grew up", False),
                ("(B) Growing up", True),
                ("(C) To grow up", False),
                ("(D) She had grown up", False),
            ],
            "explanation": (
                "The sentence needs an introductory participial phrase whose implied subject matches "
                "the subject of the main clause, 'the painter'. Choice (B) 'Growing up in a remote "
                "mountain village' is a present participial phrase that correctly implies the painter "
                "grew up in that village, and the main clause subject ('the painter') is the one "
                "doing the growing. Choice (A) creates a run-on sentence. Choice (C) 'To grow up' "
                "implies purpose, which is illogical here. Choice (D) also creates a run-on."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The investigators found evidence of tampering in the locked cabinet, ______ the "
                "case considerably.\n\n"
                "(A) which complicated\n"
                "(B) complicating\n"
                "(C) that complicated\n"
                "(D) it complicated"
            ),
            "difficulty": 3,
            "choices": [
                ("(A) which complicated", False),
                ("(B) complicating", True),
                ("(C) that complicated", False),
                ("(D) it complicated", False),
            ],
            "explanation": (
                "A participial phrase at the end of a sentence can modify the action or result of "
                "the main clause. Choice (B) 'complicating the case considerably' is a participial "
                "phrase that correctly and concisely modifies the entire action of finding the "
                "evidence. Choice (A) 'which complicated' would require the relative clause to "
                "refer specifically to 'the locked cabinet', which is an awkward misplaced "
                "reference. Choice (C) 'that complicated' would create a restrictive relative clause "
                "that illogically modifies 'cabinet'. Choice (D) creates a run-on sentence."
            ),
        },
        # --- Lesson 5: Parallel Structure (4 questions) ---
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The new urban planning initiative aims to increase green spaces, ______, and "
                "provide affordable housing for low-income residents.\n\n"
                "(A) improving public transportation\n"
                "(B) improved public transportation\n"
                "(C) improve public transportation\n"
                "(D) to improve public transportation"
            ),
            "difficulty": 1,
            "choices": [
                ("(A) improving public transportation", False),
                ("(B) improved public transportation", False),
                ("(C) improve public transportation", True),
                ("(D) to improve public transportation", False),
            ],
            "explanation": (
                "The sentence contains a parallel series of infinitive phrases: 'to increase', "
                "___, and 'provide' (with 'to' implied). All items in the series must share the "
                "same grammatical form -- in this case, bare infinitives. Choice (C) 'improve' "
                "matches the form of 'increase' and 'provide'. Choice (A) uses a gerund. Choice "
                "(B) uses a past participle. Choice (D) adds 'to' which breaks the parallel "
                "pattern when the first 'to' is shared across all items."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The documentary was praised not only for ______ but also for the depth of "
                "its research.\n\n"
                "(A) its stunning cinematography\n"
                "(B) how stunning the cinematography was\n"
                "(C) the cinematography being stunning\n"
                "(D) a stunning way to film things"
            ),
            "difficulty": 2,
            "choices": [
                ("(A) its stunning cinematography", True),
                ("(B) how stunning the cinematography was", False),
                ("(C) the cinematography being stunning", False),
                ("(D) a stunning way to film things", False),
            ],
            "explanation": (
                "The correlative conjunction 'not only...but also' requires parallel structure on "
                "both sides. The second element is 'the depth of its research' -- a noun phrase. "
                "The first element must also be a noun phrase. Choice (A) 'its stunning "
                "cinematography' is a noun phrase that parallels 'the depth of its research'. "
                "Choice (B) is a noun clause, not a simple noun phrase. Choice (C) uses a gerund "
                "construction that is awkward and non-parallel. Choice (D) uses a different noun "
                "phrase structure that changes the intended meaning."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The senator argued that the proposed legislation was both fiscally irresponsible "
                "and ______.\n\n"
                "(A) it would be constitutionally questionable\n"
                "(B) constitutionally questionable\n"
                "(C) a constitutional question\n"
                "(D) questioning the constitution"
            ),
            "difficulty": 2,
            "choices": [
                ("(A) it would be constitutionally questionable", False),
                ("(B) constitutionally questionable", True),
                ("(C) a constitutional question", False),
                ("(D) questioning the constitution", False),
            ],
            "explanation": (
                "The correlative conjunction 'both...and' requires parallel grammatical structures "
                "on both sides. The first element is 'fiscally irresponsible' -- an adverb + "
                "adjective construction. Choice (B) 'constitutionally questionable' matches this "
                "pattern exactly (adverb + adjective). Choice (A) adds a subject and verb, "
                "breaking the parallelism. Choice (C) 'a constitutional question' is a noun phrase, "
                "not an adjective phrase. Choice (D) uses a participial phrase."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The new employee was diligent, creative, ______.\n\n"
                "(A) and she always arrived on time\n"
                "(B) and punctual\n"
                "(C) and being punctual\n"
                "(D) and she had punctuality"
            ),
            "difficulty": 3,
            "choices": [
                ("(A) and she always arrived on time", False),
                ("(B) and punctual", True),
                ("(C) and being punctual", False),
                ("(D) and she had punctuality", False),
            ],
            "explanation": (
                "The series lists qualities of the new employee: 'diligent', 'creative', and ___. "
                "All items are single adjectives, so the third item must also be a single adjective. "
                "Choice (B) 'and punctual' maintains the parallel list of adjectives. Choice (A) "
                "adds a full clause, breaking the parallel structure. Choice (C) 'being punctual' "
                "is a gerund phrase, not an adjective. Choice (D) 'she had punctuality' is a full "
                "clause with a noun."
            ),
        },
        # --- Lesson 6: Punctuation (5 questions) ---
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The expedition team faced three major challenges ______ extreme weather "
                "conditions, a shortage of supplies, and communication failures.\n\n"
                "(A) ;\n"
                "(B) ,\n"
                "(C) :\n"
                "(D) --"
            ),
            "difficulty": 1,
            "choices": [
                ("(A) ;", False),
                ("(B) ,", False),
                ("(C) :", True),
                ("(D) --", False),
            ],
            "explanation": (
                "A colon is used to introduce a list or explanation when the clause before the "
                "colon is a complete independent clause. 'The expedition team faced three major "
                "challenges' is a complete independent clause, and the list that follows "
                "elaborates on those challenges. Choice (C) ':' is correct. Choice (A) ';' joins "
                "two independent clauses but the material after it is not a full independent "
                "clause. Choice (B) ',' is too weak to introduce a formal list in this context. "
                "Choice (D) '--' (em dash) could work stylistically but a colon is the standard "
                "convention for introducing a formal list after a complete clause."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The study's conclusions were widely accepted ______ its methodology was later "
                "shown to contain serious errors.\n\n"
                "(A) , however\n"
                "(B) ; however,\n"
                "(C) , however,\n"
                "(D) however,"
            ),
            "difficulty": 2,
            "choices": [
                ("(A) , however", False),
                ("(B) ; however,", True),
                ("(C) , however,", False),
                ("(D) however,", False),
            ],
            "explanation": (
                "The word 'however' is a conjunctive adverb, not a coordinating conjunction. It "
                "cannot join two independent clauses with just a comma -- that would be a comma "
                "splice. The correct punctuation is a semicolon before 'however' and a comma after "
                "it. Choice (B) '; however,' is the only correct option. Choice (A) creates a "
                "comma splice. Choice (C) also creates a comma splice by using a comma before "
                "'however'. Choice (D) creates a fused sentence."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The architect's design -- bold, unconventional, and entirely unlike anything "
                "seen before ______ won the international competition by a unanimous vote.\n\n"
                "(A) ,\n"
                "(B) ;\n"
                "(C) :\n"
                "(D) --"
            ),
            "difficulty": 2,
            "choices": [
                ("(A) ,", False),
                ("(B) ;", False),
                ("(C) :", False),
                ("(D) --", True),
            ],
            "explanation": (
                "The sentence uses a pair of em dashes to set off a parenthetical description. "
                "When a parenthetical element is introduced with an em dash, it must be closed "
                "with another em dash. The opening dash appears after 'design', so the closing "
                "dash must appear after 'before' to complete the interruption. Choice (D) '--' "
                "correctly closes the parenthetical. Choice (A) using a comma would create an "
                "asymmetric pair (dash...comma). Choices (B) and (C) are not used to close "
                "parenthetical em dash phrases."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "Maria submitted the report on time ______ she had barely slept the night before.\n\n"
                "(A) , although\n"
                "(B) ; although\n"
                "(C) although,\n"
                "(D) although"
            ),
            "difficulty": 1,
            "choices": [
                ("(A) , although", True),
                ("(B) ; although", False),
                ("(C) although,", False),
                ("(D) although", False),
            ],
            "explanation": (
                "The word 'although' is a subordinating conjunction that introduces a dependent "
                "clause. When a dependent clause follows an independent clause, they can be joined "
                "with a comma + subordinating conjunction. Choice (A) ', although' correctly joins "
                "the independent clause to the dependent clause. Choice (B) is incorrect because a "
                "semicolon must be followed by an independent clause, but 'although she had barely "
                "slept' is dependent. Choice (C) places the comma incorrectly after 'although'. "
                "Choice (D) creates a run-on by omitting the comma."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The journalist interviewed four witnesses ______ a retired teacher, a shop owner, "
                "a police officer, and a student.\n\n"
                "(A) :\n"
                "(B) ,\n"
                "(C) ;\n"
                "(D) --"
            ),
            "difficulty": 3,
            "choices": [
                ("(A) :", True),
                ("(B) ,", False),
                ("(C) ;", False),
                ("(D) --", False),
            ],
            "explanation": (
                "A colon is used after a complete independent clause to introduce a list. 'The "
                "journalist interviewed four witnesses' is a complete independent clause, and the "
                "list that follows names those witnesses. Choice (A) ':' is correct. Choice (B) "
                "',' is insufficient to formally introduce an appositive list. Choice (C) ';' is "
                "used between independent clauses, but the material after the blank is not an "
                "independent clause. Choice (D) '--' is possible stylistically, but a colon is "
                "the standard and most precise choice for introducing an explanatory list."
            ),
        },
        # --- Lesson 7: Verb Tense and Consistency (5 questions) ---
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "By the time the rescue team arrived at the summit, the climbers ______ waiting "
                "for more than eighteen hours.\n\n"
                "(A) were\n"
                "(B) had been\n"
                "(C) have been\n"
                "(D) are"
            ),
            "difficulty": 1,
            "choices": [
                ("(A) were", False),
                ("(B) had been", True),
                ("(C) have been", False),
                ("(D) are", False),
            ],
            "explanation": (
                "The phrase 'By the time...arrived' signals that one past action (waiting) was "
                "completed before another past action (the team arriving). To express an action "
                "completed before another past action, use the past perfect tense. Choice (B) "
                "'had been' is the correct past perfect progressive form. Choice (A) 'were' is "
                "simple past and does not convey the sequence clearly. Choice (C) 'have been' is "
                "present perfect, which is used for actions relevant to the present -- not here. "
                "Choice (D) 'are' is present tense."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "In the novel, the protagonist travels across the country and ______ the true "
                "meaning of her family's history.\n\n"
                "(A) discovered\n"
                "(B) had discovered\n"
                "(C) discovers\n"
                "(D) will discover"
            ),
            "difficulty": 1,
            "choices": [
                ("(A) discovered", False),
                ("(B) had discovered", False),
                ("(C) discovers", True),
                ("(D) will discover", False),
            ],
            "explanation": (
                "When describing events in a literary work, writers use the literary present tense "
                "(simple present). The first verb 'travels' is in the present tense, so the second "
                "verb must also be present to maintain consistency. Choice (C) 'discovers' is the "
                "correct present tense form. Choice (A) 'discovered' shifts to the past tense "
                "without reason. Choice (B) 'had discovered' is past perfect, implying discovery "
                "before the traveling -- illogical here. Choice (D) 'will discover' is future tense."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "If the funding ______ approved next month, the laboratory would be able to hire "
                "five additional researchers.\n\n"
                "(A) is\n"
                "(B) was\n"
                "(C) were\n"
                "(D) will be"
            ),
            "difficulty": 2,
            "choices": [
                ("(A) is", False),
                ("(B) was", False),
                ("(C) were", True),
                ("(D) will be", False),
            ],
            "explanation": (
                "The sentence expresses a hypothetical or conditional situation: the funding is not "
                "yet approved. The main clause uses 'would be able to', which signals a conditional "
                "statement. In formal English, a conditional if-clause expressing a hypothetical "
                "situation uses the subjunctive mood: 'were' instead of 'was'. Choice (C) 'were' is "
                "the correct subjunctive form. Choice (A) 'is' would be used for a real conditional "
                "('If the funding is approved, we will hire'). Choice (B) 'was' is the indicative "
                "past, not the subjunctive. Choice (D) 'will be' creates a tense mismatch with the "
                "conditional 'would'."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The researchers ______ three potential vaccine candidates since the outbreak began "
                "two years ago.\n\n"
                "(A) identified\n"
                "(B) have identified\n"
                "(C) had identified\n"
                "(D) identify"
            ),
            "difficulty": 2,
            "choices": [
                ("(A) identified", False),
                ("(B) have identified", True),
                ("(C) had identified", False),
                ("(D) identify", False),
            ],
            "explanation": (
                "The phrase 'since the outbreak began two years ago' signals an action that started "
                "in the past and continues to be relevant in the present. This is the classic "
                "context for the present perfect tense. Choice (B) 'have identified' is the correct "
                "present perfect form. Choice (A) 'identified' is simple past, which would suggest "
                "the identification is entirely finished and disconnected from the present. Choice "
                "(C) 'had identified' is past perfect, used for actions completed before another "
                "past action. Choice (D) 'identify' is simple present."
            ),
        },
        {
            "text": (
                "Which choice completes the text so that it conforms to the conventions of "
                "Standard Written English?\n\n"
                "The engineer reviewed the blueprints, identified the structural flaw, and "
                "______ a detailed report to the project director.\n\n"
                "(A) submits\n"
                "(B) is submitting\n"
                "(C) submitted\n"
                "(D) had submitted"
            ),
            "difficulty": 3,
            "choices": [
                ("(A) submits", False),
                ("(B) is submitting", False),
                ("(C) submitted", True),
                ("(D) had submitted", False),
            ],
            "explanation": (
                "The sentence lists three actions performed by the engineer in sequence: 'reviewed', "
                "'identified', and ___. Tense consistency requires that all three verbs be in the "
                "same tense. The first two verbs 'reviewed' and 'identified' are simple past, so "
                "the third verb must also be simple past. Choice (C) 'submitted' is correct. "
                "Choice (A) 'submits' is present tense -- inconsistent with the past narrative. "
                "Choice (B) 'is submitting' is present progressive. Choice (D) 'had submitted' is "
                "past perfect, which would imply submission occurred before the review -- illogical "
                "given the sequential narrative."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Seed SAT RW Standard English Conventions"

    def handle(self, *args, **options):
        course, _ = Course.objects.update_or_create(
            slug=COURSE["slug"],
            defaults={
                "title": COURSE["title"],
                "program": COURSE["program"],
                "subject": COURSE["subject"],
                "description": COURSE["description"],
            },
        )
        course.lessons.all().delete()
        for order, (title, content) in enumerate(COURSE["lessons"], start=1):
            Lesson.objects.create(course=course, title=title, content=content, order=order)
        course.questions.all().delete()
        for item in COURSE["mcqs"]:
            q = Question.objects.create(
                course=course,
                text=item["text"],
                qtype="mcq",
                difficulty=item["difficulty"],
                explanation=item["explanation"],
            )
            for text, is_correct in item["choices"]:
                Choice.objects.create(question=q, text=text, is_correct=is_correct)
        self.stdout.write(
            self.style.SUCCESS(
                f"Created '{course.title}' with {len(COURSE['lessons'])} lessons "
                f"and {len(COURSE['mcqs'])} questions."
            )
        )
