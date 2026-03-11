import React,{useEffect,useState} from "react";

import 'bootstrap/dist/css/bootstrap.min.css';

import TaskForm from "./components/TaskForm";
import Filters from "./components/Filters";
import TaskTable from "./components/TaskTable";

import {getTasks} from "./api";

function App(){

const [tasks,setTasks] = useState([]);

const loadTasks = async(query="") => {

const data = await getTasks(query);

setTasks(data);

}

useEffect(()=>{
loadTasks();
},[])

return(

<div className="container mt-5">

<h2 className="text-center mb-4">Task Manager</h2>

<TaskForm reload={loadTasks}/>

<Filters reload={loadTasks}/>

<TaskTable tasks={tasks} reload={loadTasks}/>

</div>

)

}

export default App