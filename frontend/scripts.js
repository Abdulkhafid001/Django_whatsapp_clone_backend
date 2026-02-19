async function signUp(route, data) {
  try {
    const response = await fetch(route, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzcxNDM5MDEwLCJpYXQiOjE3NzEzNTI2MTAsImp0aSI6ImJjYTJlZTBjNTQ4NjQ1MGJhYTg3OWZlNDAzNzQ1ODM2IiwidXNlcl9pZCI6IjEifQ.6LTwXDAOFXBwdxBOJgh8r34Ajt45K1iCy0d3sALT4Ug",
      },
      body: JSON.stringify(data),
    });
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
    const responseData = await response.json();
    console.log(responseData.data.username);
    console.log(responseData.tokens);
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
