

function setAttributes(element, attributes) {
    Object.keys(attributes).forEach(attr => {
        element.setAttribute(attr, attributes[attr]);
    });
}

function add_question(num_of_questions) {
    if (num_of_questions < 20) {
        let questions = document.getElementById('questions');

        let li = document.createElement('li');
        let h5 = document.createElement('h5');
        h5.appendChild(document.createTextNode(`Вопрос №${questions.childElementCount + 1}`));
        li.appendChild(h5);
        let question = document.createElement('input');
        setAttributes(question, {
            type: 'text',
            placeholder: 'Ваш вопрос',
            name: `question_${questions.childElementCount + 1}`,
            required: 'required',
            class: 'form-control m-1',
        });
        li.appendChild(question);
        let div = document.createElement('div');
        let ol = document.createElement('ol');
        setAttributes(ol, {
            name: `answers_${questions.childElementCount + 1}`,
            id: `answers_${questions.childElementCount + 1}`
        });
        for (let i = 0; i < 2; i++)
            add_answer(ol.childElementCount + 1, questions.childElementCount + 1, ol);
        let input_new_ans = document.createElement('input');
        setAttributes(input_new_ans, {
            type: 'button',
            name: `${questions.childElementCount + 1}`,
            onclick: `add_answer(document.getElementById('answers_${questions.childElementCount + 1}').childElementCount+1, ${questions.childElementCount + 1}, document.getElementById('answers_${questions.childElementCount + 1}'))`,
            value: 'Добавить вариант ответа',
            class: 'btn btn-success m-1',
        });
        let input_del_ans = document.createElement('input');
        setAttributes(input_del_ans, {
            type: 'button',
            name: `${questions.childElementCount + 1}`,
            onclick: `remove_answer(document.getElementById('answers_${questions.childElementCount + 1}'))`,
            value: 'Удалить вариант ответа',
            class: 'btn btn-danger m-1',
        });
        div.appendChild(ol);
        div.appendChild(input_new_ans);
        div.appendChild(input_del_ans);
        li.appendChild(div);

        let ol_correct_answers = document.createElement('ol');
        setAttributes(ol_correct_answers, {
            id: `correct_answer_${questions.childElementCount + 1}`
        });
        let input_correct_answer = document.createElement('input');
        setAttributes(input_correct_answer, {
            type: 'text',
            placeholder: 'Правильный ответ',
            name: `correct_answer_${ol_correct_answers.id.split('_')[2]}_${ol_correct_answers.childElementCount + 1}`,
            required: 'required',
            class: 'form-control m-1',
        });
        let li_correct_answer = document.createElement('li');
        li_correct_answer.appendChild(input_correct_answer);
        ol_correct_answers.appendChild(li_correct_answer);
        li.appendChild(ol_correct_answers);
        let input_add_correct_answer = document.createElement('input');
        let input_del_correct_answer = document.createElement('input');
        setAttributes(input_add_correct_answer, {
            type: 'button',
            onclick: `add_correct_answer(document.getElementById('answers_${ol.id.split('_')[1]}'),document.getElementById('correct_answer_${ol_correct_answers.id.split('_')[2]}'))`,
            value: 'Добавить правильный вариант ответа',
            class: 'btn btn-success m-1',
        });
        setAttributes(input_del_correct_answer, {
            type: 'button',
            onclick: `del_correct_answer(document.getElementById('correct_answer_${ol_correct_answers.id.split('_')[2]}'))`,
            value: 'Удалить правильный вариант ответа',
            class: 'btn btn-danger m-1',
        });
        li.appendChild(input_add_correct_answer);
        li.appendChild(input_del_correct_answer);
        questions.appendChild(li);
    }
}

function remove_question(li) {
    if (li.parentElement.childElementCount > 1)
        li.remove();
}

function add_answer(cur_answer, cur_question, ol) {
    if (ol.childElementCount < 20) {
        let li = document.createElement('li');
        let input = document.createElement('input');
        setAttributes(input, {
            type: 'text',
            placeholder: 'Вариант ответа',
            name: `answer_${cur_question}_${cur_answer}`,
            required: 'required',
            class: 'form-control m-1',
        });
        li.appendChild(input);
        ol.appendChild(li);
    }
}

function remove_answer(ol) {
    if (ol.childElementCount > 2) {
        ol.lastChild.remove();
        let correct_answers = document.getElementById(`correct_answer_${ol.id.split('_')[1]}`);
        if (correct_answers.childElementCount > ol.childElementCount) {
            correct_answers.lastChild.remove();
        }
    }
}

function add_correct_answer(ol_answers, ol_correct_answer) {
    if (ol_correct_answer.childElementCount < ol_answers.childElementCount) {
        let li = document.createElement('li');
        let input = document.createElement('input');
        setAttributes(input, {
            type: 'text',
            placeholder: 'Правильный ответ',
            name: `correct_answer_${ol_answers.id.split('_')[1]}_${ol_correct_answer.childElementCount + 1}`,
            required: 'required',
            class: 'form-control m-1',
        });
        li.appendChild(input);
        ol_correct_answer.appendChild(li);
    }
}

function del_correct_answer(ol_correct_answer) {
    if (ol_correct_answer.childElementCount > 1) {
        ol_correct_answer.lastChild.remove();
    }
}