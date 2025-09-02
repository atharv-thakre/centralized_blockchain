// static/app.js

const API_BASE = "/";

document.getElementById("createBtn").addEventListener("click", async () => {
  const roll_no = document.getElementById("roll_no").value.trim();
  const name = document.getElementById("name").value.trim();
  const marks = parseInt(document.getElementById("marks").value, 10);

  if (!roll_no || !name || isNaN(marks)) {
    alert("Please fill all fields correctly.");
    return;
  }

  const res = await fetch(API_BASE + "students", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ roll_no, name, marks }),
  });

  const resultDiv = document.getElementById("createResult");
  if (res.ok) {
    const data = await res.json();
    resultDiv.innerHTML = `<pre>Created: ${JSON.stringify(data, null, 2)}</pre>`;
    document.getElementById("roll_no").value = "";
    document.getElementById("name").value = "";
    document.getElementById("marks").value = "";
  } else {
    const err = await res.json();
    resultDiv.innerHTML = `<pre style="color:red">${JSON.stringify(err, null, 2)}</pre>`;
  }
});

document.getElementById("fetchBtn").addEventListener("click", async () => {
  const res = await fetch(API_BASE + "students");
  const out = document.getElementById("studentsList");
  if (res.ok) {
    const list = await res.json();
    if (list.length === 0) {
      out.innerHTML = "<i>No students yet</i>";
      return;
    }
    out.innerHTML = list.map(s => `<div><b>${s.roll_no}</b> — ${s.name} — Marks: ${s.marks}</div>`).join("");
  } else {
    out.innerHTML = "Error fetching students";
  }
});

document.getElementById("fetchChain").addEventListener("click", async () => {
  const res = await fetch(API_BASE + "blockchain");
  const area = document.getElementById("chainArea");
  if (res.ok) {
    const blocks = await res.json();
    area.innerHTML = blocks.map(b => `
      <div style="border:1px solid #ddd; padding:8px; margin:8px 0;">
        <b>Index:</b> ${b.index} <b>Timestamp:</b> ${b.timestamp}<br/>
        <b>Data:</b> <pre>${b.data}</pre>
        <b>Prev:</b> ${b.previous_hash}<br/>
        <b>Hash:</b> ${b.hash}
      </div>
    `).join("");
  } else {
    area.innerHTML = "Error fetching blockchain";
  }
});

document.getElementById("validateChain").addEventListener("click", async () => {
  const res = await fetch(API_BASE + "validate");
  const area = document.getElementById("chainArea");
  if (res.ok) {
    const json = await res.json();
    area.innerHTML = `<div><b>Valid:</b> ${json.valid}</div>` + area.innerHTML;
  } else {
    area.innerHTML = "Error validating chain";
  }
});
