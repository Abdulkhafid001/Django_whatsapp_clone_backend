async function login(url, data) {
  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzcxNjI0NjE5LCJpYXQiOjE3NzE1MzgyMTksImp0aSI6IjQ2YTY4MjFhMGNlNzQyMTliZDIyNmQ1ZjlhNjc2ZGZjIiwidXNlcl9pZCI6IjEifQ.HTlcq2wSRUDnAGDBqZwaMrzV1TOxQbCt37LzUhPCLs0",
      },
      body: JSON.stringify(data),
    });
    const serverResponse = await response.json();
    console.log(serverResponse);
    // save username and accesstoken  to localstorage
    localStorage.setItem('username', serverResponse.username);
    localStorage.setItem("userAccessTokenLogin", serverResponse.accesstoken);
    const loginSuccessful = serverResponse.loginSuccessful;
    console.log(typeof loginSuccessful);
    if (loginSuccessful == true) {
      window.location.href =
        "C:/Users/USER/Documents/Code Folders/Django_whatsapp_clone_backend/frontend/home.html";
    }
  } catch (error) {
    console.error("Errors:", error);
  }
}

document.querySelector("form").addEventListener("submit", (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const formObject = Object.fromEntries(formData.entries());
  login("http://127.0.0.1:8000/customauth/login/", formObject);
});

const passwordInput = document.getElementById("password");
const toggleButton = document.getElementById("togglePassword");

toggleButton.addEventListener("click", function () {
  const type =
    passwordInput.getAttribute("type") === "password" ? "text" : "password";
  passwordInput.setAttribute("type", type);
  this.textContent = type === "password" ? "👁" : "🙈";
});
