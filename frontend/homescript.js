async function logout(url, data) {
  const request = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("userAccessTokenLogin")}`,
    },
    body: JSON.stringify(data),
  });
  const responseData = await request.json();
  console.log(responseData);
}
const getUsernameLocalStorage = localStorage.getItem("username");

const usernamePlaceholder = document.getElementById("showUsername").textContent = getUsernameLocalStorage;

// logout impl
const data = {username: usernamePlaceholder}
const logoutForm = document.getElementById("logoutForm").addEventListener("submit", function (event) {
    event.preventDefault();
    logout('http://127.0.0.1:8000/customauth/logout/', data);
});
