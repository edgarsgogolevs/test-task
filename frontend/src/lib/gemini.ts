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
    console.log('Fetching models...');
    const response = await fetch(apiUrl + '/gemini/models');
    if (!response.ok) throw new Error('Failed to fetch models');
    const data = await response.json();
    if (!data.models) throw new Error('Failed to fetch models');
    return data.models;
  } catch (error) {
    showError(error as Error);
    throw error;
  }
}
