// SAMPLE
export function request(path) {
  return fetch(path).then(r => r.json());
}

export function post(path, body) {
  return fetch(path, { method: 'POST', body: JSON.stringify(body) });
}
