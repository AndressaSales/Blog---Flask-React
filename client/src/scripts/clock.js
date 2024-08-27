//Clock
export default function getCurrentDateTime() {
    const now = new Date();
    const hour = now.getHours();
    const minute = now.getMinutes();
    const second = now.getSeconds();
    const day = now.getDate();
    const month = now.getMonth() + 1;
    // Months are 0-based
    const year = now.getFullYear();
  
    return {
      hour,
      minute,
      second,
      day,
      month,
      year
    }
  }