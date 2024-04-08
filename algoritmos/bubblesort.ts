function Bubblesort(v: number[]) {
  for (var i = v.length - 1; i > 0; i--) {
    var changes = 0;
    for (var j = 0; j < i; j++) {
      if (v[j] > v[j + 1]) {
        let aux = v[i];
        v[j] = v[j + 1];
        v[j + 1] = aux;
        changes++;
      }
    }
    if (changes <= 1) break;
  }
}
