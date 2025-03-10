import { showError } from '@/lib/notify';

const apiUrl = import.meta.env.VITE_API_URL;
const headers = {
  'Content-Type': 'application/json',
};

export function queryGemini(query: string, model: string): Promise<Response> {
  return fetch(apiUrl + '/gemini/query', {
    method: 'POST',
    headers: headers,
    body: JSON.stringify({
      query,
      model,
    }),
  });
}

export async function getAvailableModels(): Promise<string[]> {
  try {
    const response = await fetch(apiUrl + '/gemini/models');
    const data = await response.json();
    return data.models;
  } catch (error) {
    console.error(error);
    showError(error as Error);
    return Promise.reject(error);
  }
}
