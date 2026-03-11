import React,{useState} from "react";

function Filters({reload}){

const [priority,setPriority] = useState("");
const [status,setStatus] = useState("");

const applyFilters = ()=>{

let params=[];

if(priority){
params.push(`priority=${priority}`);
}

if(status!==""){
params.push(`completed=${status}`);
}

reload(params.join("&"));

}

return(

<div className="card p-3 mb-3">

<div className="row">

<div className="col">

<select
className="form-select"
value={priority}
onChange={(e)=>setPriority(e.target.value)}
>

<option value="">All Priority</option>
<option value="Low">Low</option>
<option value="Medium">Medium</option>
<option value="High">High</option>

</select>

</div>

<div className="col">

<select
className="form-select"
value={status}
onChange={(e)=>setStatus(e.target.value)}
>

<option value="">All Status</option>
<option value="true">Completed</option>
<option value="false">Pending</option>

</select>

</div>

<div className="col">

<button
className="btn btn-success"
onClick={applyFilters}
>

Apply Filters

</button>

</div>

</div>

</div>

)

}

export default Filters