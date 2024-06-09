const add_input = document.querySelector('.input');
const submit_btn = document.querySelector('.add');
const delete_btns = document.getElementsByClassName('del');
let task_dev = document.querySelector('.tasks');

let tasks = [];
if (localStorage.getItem('tasks')) {
  tasks = JSON.parse(localStorage.getItem('tasks'));
  add_task_to_html(tasks);
}

const addTask = (task_text) => {
  const task = {
    id: Date.now(),
    title: task_text,
    completed: false,
  };
  tasks.push(task);
  add_task_to_html(tasks);
  add_tasks_to_local_storage(tasks);
}

const add_tasks_to_local_storage = (tasks) => {
  window.localStorage.setItem('tasks', JSON.stringify(tasks))
}

// const get_tasks_from_local_storage = () => {
//   let data = window.localStorage.getItem(tasks);
//   if (data) {
//     tasks = JSON.parse(data);
//     add_task_to_html(tasks);
//   }
// }

// get_tasks_from_local_storage()

function add_task_to_html(tasks) {
  let tasks_cont = document.querySelector(".tasks")
  tasks_cont.innerHTML = "";
  tasks.forEach((task) => {
    let div = document.createElement("div");
    div.className = "task";
    if (task.completed) {
      div.className = "task done";
    }
    div.setAttribute("data_id", task.id)
    div.appendChild(document.createTextNode(task.title));
    let span = document.createElement("span");
    span.className = "del";
    span.appendChild(document.createTextNode("X"));
    div.appendChild(span);
    tasks_cont.appendChild(div);
  })
}


submit_btn.addEventListener('click', (e) => {
  if(add_input.value == "") {
    alert('Please enter a value');
  } else {
    addTask(add_input.value);
    add_input.value = "";
  }
});


const delete_from_local_storage = (taskId) => {
  new_tasks = tasks.filter((task) => task.id !== taskId);
  add_tasks_to_local_storage(new_tasks) 
}


// activate the delete button
task_dev.addEventListener('click', (e) => {
  if (e.target.classList.contains('del')) {
    delete_from_local_storage(e.target.parentElement.getAttribute('data-id'));
    e.target.parentElement.remove();
  }
  if (e.target.classList.contains('task')) {
    e.target.classList.toggle('done');
  }
});



