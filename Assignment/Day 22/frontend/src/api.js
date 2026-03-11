const BASE_URL = "http://127.0.0.1:5000";

export const getTasks = async (query="") => {

  const res = await fetch(`${BASE_URL}/tasks?${query}`);

  return res.json();
};

export const createTask = async (task) => {

  await fetch(`${BASE_URL}/tasks`, {

    method: "POST",

    headers: {
      "Content-Type": "application/json"
    },

    body: JSON.stringify(task)
  });
};

export const toggleTask = async (id) => {

  await fetch(`${BASE_URL}/tasks/${id}/toggle`, {
    method: "PUT"
  });
};

export const deleteTask = async (id) => {

  await fetch(`${BASE_URL}/tasks/${id}`, {
    method: "DELETE"
  });
};