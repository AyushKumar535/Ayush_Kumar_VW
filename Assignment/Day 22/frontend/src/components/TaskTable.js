import React from "react";

import {toggleTask,deleteTask} from "../api";

function TaskTable({tasks,reload}){

const toggle = async(id)=>{

await toggleTask(id);

reload();

}

const remove = async(id)=>{

await deleteTask(id);

reload();

}

return(

<table className="table table-bordered">

<thead className="table-dark">

<tr>

<th>Title</th>
<th>Priority</th>
<th>Status</th>
<th>Created</th>
<th>Action</th>

</tr>

</thead>

<tbody>

{tasks.map((t)=>(

<tr key={t.id}>

<td>{t.title}</td>

<td>

<span className={`badge bg-${
t.priority==="High"
?"danger"
:t.priority==="Medium"
?"warning"
:"success"
}`}>

{t.priority}

</span>

</td>

<td>

{t.completed ? "Completed" : "Pending"}

</td>

<td>

{new Date(t.created_at).toLocaleString()}

</td>

<td>

<button
className="btn btn-sm btn-info me-2"
onClick={()=>toggle(t.id)}
>

Toggle

</button>

<button
className="btn btn-sm btn-danger"
onClick={()=>remove(t.id)}
>

Delete

</button>

</td>

</tr>

))}

</tbody>

</table>

)

}

export default TaskTable