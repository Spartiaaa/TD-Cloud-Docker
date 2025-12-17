import { API_BASE_URL } from "./config.js";

/**
 * Fonction générique pour faire les appels API
 */
async function request(endpoint, method = "GET", data = null) {
  const url = `${API_BASE_URL}${endpoint}`;
  const options = {
    method,
    headers: { "Content-Type": "application/json" },
  };
  if (data) options.body = JSON.stringify(data);

  try {
    const response = await fetch(url, options);
    if (!response.ok) {
      const errorData = await response
        .json()
        .catch(() => ({ detail: response.statusText }));
      throw new Error(errorData.detail || `Erreur ${response.status}`);
    }
    if (response.status === 204) return null; // DELETE retourne parfois 204
    return await response.json();
  } catch (err) {
    console.error("API Error:", err);
    throw err;
  }
}

/* ==========================
   HÔTELS
========================== */
export const getHotels = () => request("/hotels/"); // Liste de tous les hôtels
export const getHotel = (id) => request(`/hotels/${id}`); // Détail d’un hôtel
export const createHotel = (data) => request("/hotels/", "POST", data);
export const deleteHotel = (id) => request(`/hotels/${id}`, "DELETE");

/* ==========================
   CHAMBRES
========================== */
export const getChambresByHotel = (hotel_id) =>
  request(`/chambres/${hotel_id}`);
export const createChambre = (data) => request("/chambres/", "POST", data);
export const updateChambre = (id, data) =>
  request(`/chambres/${id}`, "PUT", data);
export const getEtatChambre = (id) => request(`/chambres/${id}`);

/* ==========================
   CLIENTS
========================== */
export const getClients = () => request("/clients/"); // Liste de tous les clients
export const getClient = (id) => request(`/clients/${id}`); // Détail client
export const createClient = (data) => request("/clients/", "POST", data);
export const deleteClient = (id) => request(`/clients/${id}`, "DELETE");

/* ==========================
   RÉSERVATIONS
========================== */
export const getReservations = () => request("/reservations/");
export const createReservation = (data) =>
  request("/reservations/", "POST", data);
export const deleteReservation = (id) =>
  request(`/reservations/${id}`, "DELETE");
