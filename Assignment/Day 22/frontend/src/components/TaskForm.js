import React,{useState} from "react";

import {createTask} from "../api";

function TaskForm({reload}){

const [title,setTitle] = useState("");
const [priority,setPriority] = useState("Low");

const submit = async(e)=>{

e.preventDefault();

await createTask({title,priority});

setTitle("");

reload();
}

return(

<form onSubmit={submit} className="card p-3 mb-3">

<input
className="form-control mb-2"
placeholder="Task title"
value={title}
onChange={(e)=>setTitle(e.target.value)}
required
/>

<select
className="form-select mb-2"
value={priority}
onChange={(e)=>setPriority(e.target.value)}
>

<option>Low</option>
<option>Medium</option>
<option>High</option>

</select>

<button className="btn btn-primary">

Add Task

</button>

</form>

)

}

export default TaskForm