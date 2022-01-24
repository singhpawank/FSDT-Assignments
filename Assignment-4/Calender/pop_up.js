let global_date = new Date();

function openmodal(obj) {
  global_date = new Date(obj.value);
  modal = document.getElementById("modal");
  if (modal == null) return;
  modal.classList.toggle("active");
  overlay.classList.add("active");
  addEvents(global_date);
}

const closeModalButtons = document.querySelectorAll("[data-close-button]");
const overlay = document.getElementById("overlay");


overlay.addEventListener("click", () => {
  const modals = document.querySelectorAll(".modal.active");
  modals.forEach((modal) => {
    closeModal(modal);
  });
});

closeModalButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const modal = button.closest(".modal");
    closeModal(modal);
  });
});

function openModal(modal) {
  if (modal == null) return;
  modal.classList.add("active");
  overlay.classList.add("active");
}

function closeModal(modal) {
  if (modal == null) return;
  modal.classList.remove("active");
  overlay.classList.remove("active");
}

function addEvents(date) {
  let title =
    global_date.getDate() +
    " " +
    months[global_date.getMonth()] +
    " " +
    global_date.getFullYear() +
    " " +
    "Events";
  let list = event_list(events, global_date);

  let event_elements = "";

  for (let i = 0; i < list.length; i++) {
    event_elements += `<div class="alternate"><p>${
      i + 1 + ".  " + list[i][0] + "  -  " + list[i][1]
    }</p></div>`;
  }

  document.querySelector(".model-header h1").innerHTML = title;
  document.querySelector(".events").innerHTML = event_elements;
}

