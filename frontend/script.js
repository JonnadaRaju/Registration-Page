const API = "http://127.0.0.1:8000";

/* =========================
   Register Student
========================= */
async function register() {
  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const phone = document.getElementById("phone").value.trim();
  const course = document.getElementById("course").value.trim();

  if (!name || !email || !phone || !course) {
    alert("Please fill all fields");
    return;
  }

  try {
    const res = await fetch(`${API}/register`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, email, phone, course })
    });

    if (!res.ok) {
      const error = await res.json();
      alert(error.detail || "Error registering student");
      return;
    }

    alert("Student Registered Successfully!");

    // Clear form
    document.getElementById("name").value = "";
    document.getElementById("email").value = "";
    document.getElementById("phone").value = "";
    document.getElementById("course").value = "";

  } catch (err) {
    alert("Server error. Make sure backend is running.");
    console.error(err);
  }
}


/* =========================
   Load Students
========================= */
async function loadStudents() {
  try {
    const res = await fetch(`${API}/students`);
    const data = await res.json();

    const tableBody = document.getElementById("tableBody");
    const table = document.getElementById("studentsTable");

    if (data.students.length === 0) {
      tableBody.innerHTML = `
        <tr>
          <td colspan="4" style="text-align:center;">No Students Found</td>
        </tr>
      `;
    } else {
      tableBody.innerHTML = data.students
        .map(s => `
          <tr>
            <td>${s.name}</td>
            <td>${s.email}</td>
            <td>${s.phone}</td>
            <td>${s.course}</td>
          </tr>
        `)
        .join("");
    }

    // Show table only after button click
    table.style.display = "table";

  } catch (err) {
    alert("Error loading students");
    console.error(err);
  }
}