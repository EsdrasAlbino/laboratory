function Quicksort(v, start_pos, end_pos) {
  var pivot = v[start_pos];
  let l = start_pos;
  let r = end_pos;

  while (l <= r) {
    while (v[l] < pivot) l++;
    while (v[r] > pivot) r--;

    if (l <= r) {
      let aux = v[l];
      v[l] = v[r];
      v[r] = aux;

      l++;
      r--;
    }
  }

  if (start_pos < r) Quicksort(v, start_pos, r);
  if (end_pos > l) Quicksort(v, l, end_pos);

  return v;
}

var v = [1, 4, 6, 2, 3, 7, 2234, 8];
const quick_sort = Quicksort(v, 0, v.length - 1);
console.log("quick sort: ", quick_sort);
