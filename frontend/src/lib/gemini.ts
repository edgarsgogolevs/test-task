const apiUrl = import.meta.env.VITE_API_URL;

export function queryGemini(query: string, model: string): Promise<Response> {
  return fetch(apiUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      query,
      model,
    }),
  })
}
