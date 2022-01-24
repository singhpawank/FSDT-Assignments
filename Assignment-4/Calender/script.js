const months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];

const date = new Date();

const renderCalendar = () => {
  date.setDate(1);

  const monthDays = document.querySelector(".days");

  const lastDay = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDate();

  const prevLastDay = new Date(
    date.getFullYear(),
    date.getMonth(),
    0
  ).getDate();

  const firstDayIndex = date.getDay();

  const lastDayIndex = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDay();

  let nextDays = 7 - lastDayIndex - 1;

  document.querySelector(".current h1").innerHTML =
    months[date.getMonth()] + " " + date.getFullYear();

  document.querySelector(".current p").innerHTML = new Date().toDateString();

  let days = "";
  let temp = 0;
  for (let x = firstDayIndex; x > 0; x--) {
    temp += 1;

    let current_date = new Date(date);
    current_date.setDate(current_date.getDate() - x);

    let count = count_event(events, current_date);
    let b_value =
      current_date.getFullYear().toString() +
      "-" +
      (current_date.getMonth() + 1).toString() +
      "-" +
      current_date.getDate().toString();
    // console.log(b_value);

    if (count != 0)
      days += ` <div class="date-box prev-date-box">
                <div class="date prev-date">${prevLastDay - x + 1}</div>
                <div class="event"><button data-modal-target="#modal" type="button" class="button" onclick="openmodal(this)" value=${b_value}>${count}</button></div>
              </div>`;
    else
      days += ` <div class="date-box prev-date-box">
                <div class="date prev-date">${prevLastDay - x + 1}</div>
                <div class="event"></div>
              </div>`;
  }

  for (let i = 1; i <= lastDay; i++) {
    temp += 1;

    if (
      i === new Date().getDate() &&
      date.getMonth() === new Date().getMonth() &&
      date.getFullYear() === new Date().getFullYear()
    ) {
      let current_date = new Date(date);
      current_date.setDate(current_date.getDate() + i - 1);
      let count = count_event(events, current_date);
      let b_value =
        current_date.getFullYear() +
        "-" +
        (current_date.getMonth() + 1) +
        "-" +
        current_date.getDate();

      if (count != 0)
        days += ` <div class="date-box today">
                <div class="date ">${i}</div>
                <div class="event"><button data-modal-target="#modal" type="button" class="button" onclick="openmodal(this)" value=${b_value}>${count}</button></div>
              </div>`;
      else
        days += ` <div class="date-box today">
                <div class="date ">${i}</div>
                <div class="event"></div>
              </div>`;
    } else {
      let current_date = new Date(date);
      current_date.setDate(current_date.getDate() + i - 1);
      let count = count_event(events, current_date);
      let b_value =
        current_date.getFullYear() +
        "-" +
        (current_date.getMonth() + 1) +
        "-" +
        current_date.getDate();

      if (count != 0)
        days += ` <div class="date-box">
                    <div class="date ">${i}</div>
                    <div class="event"><button data-modal-target="#modal" type="button" class="button" onclick="openmodal(this)" value=${b_value}>${count}</button></div>
                  </div>`;
      else
        days += ` <div class="date-box">
                    <div class="date ">${i}</div>
                    <div class="event"></div>
                  </div>`;
    }
  }

  if (temp + nextDays < 42) nextDays += 7;

  for (let j = 1; j <= nextDays; j++) {
    let current_date = new Date(date);
    current_date.setDate(current_date.getDate() + j - 1);
    current_date.setMonth(current_date.getMonth() + 1);

    let count = count_event(events, current_date);

    let b_value =
      current_date.getFullYear() +
      "-" +
      (current_date.getMonth() + 1) +
      "-" +
      current_date.getDate();

    if (count != 0)
      days += ` <div class="date-box next-date-box">
                    <div class="date prev-date">${j}</div>
                    <div class="event"><button data-modal-target="#modal" type="button" class="button" onclick="openmodal(this)" value=${b_value}>${count}</button></div>
                  </div>`;
    else
      days += ` <div class="date-box next-date-box">
                    <div class="date prev-date">${j}</div>
                    <div class="event"></div>
                  </div>`;
  }
  monthDays.innerHTML = days;
};

document.querySelector(".prev").addEventListener("click", () => {
  date.setMonth(date.getMonth() - 1);
  if (date.getMonth() == 12) date.setFullYear(date.getFullYear() - 1);
  renderCalendar();
});

document.querySelector(".next").addEventListener("click", () => {
  date.setMonth(date.getMonth() + 1);
  renderCalendar();
});

renderCalendar();
