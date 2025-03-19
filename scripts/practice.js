(() => {

const problemAnsweredClass = 'answered';
const problemCorrectClass = 'correct';
const problemIncorrectClass = 'incorrect';
const checkmarkClass = 'checkmark';
const xmarkClass = 'xmark';

const calcOutputPrompt = 'Determine the output of this code.';

function setProblemPrompt(problemArgs)
{
    problemArgs.problemPrompt.textContent =
            problemArgs.problemData[problemArgs.currProblem].promptText;
}

function answerIsCorrect(problemArgs)
{
    const data = problemArgs.problemData[problemArgs.currProblem];

    if (data.answerInput.value === "")
        data.checkedCorrect = false;
    else
        data.checkedCorrect = data.answerInput.value === data.solutionText;

    return data.checkedCorrect;
}

function updateResultUi(problemArgs)
{
    const section = problemArgs.section;
    const marker = problemArgs.resultMarker;
    const data = problemArgs.problemData[problemArgs.currProblem];

    if (data.answerInput.value === "") {
        section.classList.remove(problemAnsweredClass);
        section.classList.remove(problemCorrectClass);
        section.classList.remove(problemIncorrectClass);
        marker.classList.remove(checkmarkClass);
        marker.classList.remove(xmarkClass);
    }
    else {
        section.classList.add(problemAnsweredClass);

        if (answerIsCorrect(problemArgs)) {
            section.classList.remove(problemIncorrectClass);
            section.classList.add(problemCorrectClass);
            marker.classList.remove(xmarkClass);
            marker.classList.add(checkmarkClass);
        }
        else {
            section.classList.remove(problemCorrectClass);
            section.classList.add(problemIncorrectClass);
            marker.classList.remove(checkmarkClass);
            marker.classList.add(xmarkClass);
        }
   }
}

function updateProblemUi(problemArgs)
{
    setProblemPrompt(problemArgs);
    updateResultUi(problemArgs);
    problemArgs.currentCounter.textContent = problemArgs.currProblem + 1;
}

function navigateProblem(problemArgs, offset)
{
    const len = problemArgs.problems.length;
    const curr = problemArgs.currProblem;

    // Normalize offset.
    offset %= len;
    
    problemArgs.problems[curr].hidden = true;

    // Go to the next question, according to offset.
    // We have to add the problem list length before the modulo operation
    // to prevent ever performing a modulo on a negative value.
    const next  = (curr + offset + len) % len;
    problemArgs.currProblem = next;
    problemArgs.problems[next].hidden = false;

    updateProblemUi(problemArgs);

    return next;
}

function submitAnswer(problemArgs)
{
    let curr = problemArgs.currProblem;
    const problem = problemArgs.problemData[curr];

    // If the answer was already checked and was correct, move to the
    // next problem instead.
    if (problem.checkedCorrect) {
        curr = navigateProblem(problemArgs, 1);
    }
    // Check the answer and update the ui accordingly.
    else {
        problem.checkedCorrect = answerIsCorrect(problemArgs);
        updateProblemUi(problemArgs);
    }

    problemArgs.problemData[curr].answerInput.focus();
}

// Setup practice sections.
const psections = document.getElementsByClassName('practice');
for (const sect of psections) {
    const problems = sect.querySelectorAll('&> .problem');
    const problemPrompt = sect.querySelector('.problem-prompt');
    const currentCounter = sect.querySelector('.current-problem');
    const totalCounter = sect.querySelector('.total-problems');
    const resultMarker = sect.querySelector('.answer-marker .marker');
    const prevButton = sect.querySelector('.prev-button');
    const nextButton = sect.querySelector('.next-button');
    const checkButton = sect.querySelector('.check-button');

    // Cache problem data.
    const problemData = [];
    for (const prob of problems) {
        problemData.push({
            promptText: prob.querySelector('.problem-prompt-text').value,
            solutionText: prob.querySelector('.problem-solution').value,
            answerInput: prob.querySelector('.problem-answer'),

            // Set when the problem has both been checked and was correct.
            // Used for a keyboard shortcut to determine whether to check
            // the answer or move to the next question.
            checkedCorrect: false
        });
    }

    const problemArgs = {
        section: sect,
        problems: problems,
        problemPrompt: problemPrompt,
        currentCounter: currentCounter,
        resultMarker: resultMarker,
        problemData: problemData,
        currProblem: 0
    };

    // Setup problem navigation.
    prevButton.addEventListener('click', () => {
        navigateProblem(problemArgs, -1);
    });
    nextButton.addEventListener('click', () => {
        navigateProblem(problemArgs, 1);
    });

    // Setup problem checking.
    checkButton.addEventListener('click', () => {
        submitAnswer(problemArgs);       
    });

    // Setup keyboard shortcuts.
    problemArgs.problemData.forEach(data => {
        data.answerInput.addEventListener('keydown', (e) => {
            if (e.key == 'Enter')
                submitAnswer(problemArgs);
        });
    });

    // Setup the first problem.
    problems[problemArgs.currProblem].hidden = false;
    updateProblemUi(problemArgs);
    totalCounter.textContent = problems.length;
}

})();
