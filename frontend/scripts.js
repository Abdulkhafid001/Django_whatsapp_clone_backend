async function signUp(route, data) {
  try {
    const response = await fetch(route, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzcxOTI2NDI3LCJpYXQiOjE3NzE4NDAwMjcsImp0aSI6IjdmNzQwMGUwOTI5ZTQ3ZTk4ZjcyNmY2MDc3N2E5ZDBiIiwidXNlcl9pZCI6IjEifQ.u47lrm9Tev0TawxMCx-vU6m5eqVwAalQ-wlCXOc537A",
      },
      body: JSON.stringify(data),
    });
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
    const responseData = await response.json();
    console.log(responseData.data.username);
    console.log(responseData.tokens);
    const responseMessage = document.getElementById('response-message').textContent = 'hello world';
  } catch (error) {
    console.error("Errors:", error);
  }
}

const route = "http://127.0.0.1:8000/customauth/createuser/";
const userObject = { username: "Livramento", password: "rb22030" };

// signUp(route, userObject);

const btn = document.getElementById("execute");
btn.addEventListener("click", function () {
  signUp(route, userObject);
});
