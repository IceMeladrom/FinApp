function setAttributes(element, attributes) {
    Object.keys(attributes).forEach(attr => {
        element.setAttribute(attr, attributes[attr]);
    });
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
        });
        li.appendChild(input);
        ol.appendChild(li);
        console.log(input)
    }
}

function remove_answer(ol) {
    if (ol.childElementCount > 2) {
        console.log(`${ol.lastElementChild.firstElementChild.getAttribute('name')} удален`)
        ol.lastChild.remove();
    }
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
        });
        li.appendChild(question);
        let div = document.createElement('div');
        let ol = document.createElement('ol');
        setAttributes(ol, {name: `answers_${questions.childElementCount + 1}`});
        for (let i = 0; i < 2; i++)
            add_answer(ol.childElementCount + 1, questions.childElementCount + 1, ol);
        let input_new_ans = document.createElement('input');
        setAttributes(input_new_ans, {
            type: 'button',
            onclick: 'add_answer(this.parentElement.firstElementChild.childElementCount+1, Number(this.parentElement.parentElement.children[0].textContent.split(\'№\')[1]), this.parentElement.firstElementChild)',
            value: 'Добавить вариант ответа',
        });
        let input_del_ans = document.createElement('input');
        setAttributes(input_del_ans, {
            type: 'button',
            onclick: 'remove_answer(this.parentElement.firstElementChild)',
            value: 'Удалить вариант ответа',
        });
        div.appendChild(ol);
        div.appendChild(input_new_ans);
        div.appendChild(input_del_ans);
        li.appendChild(div);
        let correct_answer = document.createElement('input');
        setAttributes(correct_answer, {
            type: 'text',
            placeholder: 'Правильный ответ',
            name: `correct_answer_${questions.childElementCount + 1}`,
            required: 'required',
        });
        li.appendChild(correct_answer);
        questions.appendChild(li);
    }
}

function remove_question(li) {
    if (li.parentElement.childElementCount > 1)
        li.remove();
}