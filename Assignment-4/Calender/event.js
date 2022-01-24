function count_event(events, date) {
  let total_events = events.length;
  let count = 0;
  for (let i = 0; i < total_events; i++) {
    let mydate = new Date(events[i][2]);
    if (
      mydate.getDate() === date.getDate() &&
      mydate.getMonth() === date.getMonth() &&
      mydate.getFullYear() === date.getFullYear()
    )
      count += 1;
  }

  return count;
}

//console.log(count_event(events, new Date("2022-01-25")));

function event_list(events, date) {
  let total_events = events.length;
  let list = [];
  for (let i = 0; i < total_events; i++) {
    let mydate = new Date(events[i][2]);
    // console.log(mydate);
    if (
      mydate.getDate() === date.getDate() &&
      mydate.getMonth() === date.getMonth() &&
      mydate.getFullYear() === date.getFullYear()
    ) {
     // console.log(events[i]);
      list.push(events[i]);
    }
  }
 // console.log(Object.keys(list).lenght);
  return list;
}
