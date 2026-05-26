// SAMPLE
export function formatDate(d) {
  return d.toISOString().slice(0, 10);
}

export function formatMoney(n) {
  return n.toFixed(2);
}
