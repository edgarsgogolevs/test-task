import { toast, type ToastOptions } from 'vue3-toastify';

const errorOpts: ToastOptions = {
  autoClose: 4000,
  position: toast.POSITION.BOTTOM_RIGHT,
};

export function showError(error: Error | string) {
  let msg : string;
  if (typeof error === 'string') {
    msg = error;
  } else {
    msg = error?.message;
  }
  toast.error(msg, errorOpts);
}
