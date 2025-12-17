/* ==========================
   1. HÔTELS
========================== */
export function renderHotelsTable(hotels) {
  const tbody = document.getElementById("table-body");
  if (!tbody) return;
  tbody.innerHTML = "";
  if (hotels.length === 0) {
    const tr = document.createElement("tr");
    tr.innerHTML = `<td colspan="4" style="text-align: center;">Aucun hôtel n'est disponible.</td>`;
    tbody.appendChild(tr);
    return;
  }
  hotels.forEach((h) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
            <td><strong>#${h.id}</strong></td>
            <td>${h.nom}</td>
            <td>${h.adresse}</td>
            <td><button class="btn-delete" data-id="${h.id}">Supprimer</button></td>
        `;
    tbody.appendChild(tr);
  });
}

/* ==========================
   2. CHAMBRES
========================== */
export function renderChambresTable(chambres) {
  const tbody = document.getElementById("table-body");
  if (!tbody) return;
  tbody.innerHTML = "";
  if (chambres.length === 0) {
    const tr = document.createElement("tr");
    tr.innerHTML = `<td colspan="5" style="text-align: center;">Aucune chambre n'est disponible.</td>`;
    tbody.appendChild(tr);
    return;
  }
  chambres.forEach((c) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
            <td><strong>${c.numero}</strong></td>
            <td>${c.type}</td>
            <td>${c.prix} €</td>
            <td>Hôtel #${c.hotel_id}</td>
            <td><button class="btn-delete" data-id="${c.id}">Supprimer</button></td>
        `;
    tbody.appendChild(tr);
  });
}

/* ==========================
   3. CLIENTS
========================== */
export function renderClientsTable(clients) {
  const tbody = document.getElementById("table-body");
  if (!tbody) return;
  tbody.innerHTML = "";
  if (clients.length === 0) {
    const tr = document.createElement("tr");
    tr.innerHTML = `<td colspan="4" style="text-align: center;">Aucun client n'est disponible.</td>`;
    tbody.appendChild(tr);
    return;
  }
  clients.forEach((c) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
            <td><strong>#${c.id}</strong></td>
            <td>${c.nom}</td>
            <td>${c.email}</td>
            <td><button class="btn-delete" data-id="${c.id}">Supprimer</button></td>
        `;
    tbody.appendChild(tr);
  });
}

/* ==========================
   4. RÉSERVATIONS
========================== */
export function renderReservationsTable(reservations) {
  const tbody = document.getElementById("table-body");
  if (!tbody) return;
  tbody.innerHTML = "";
  if (reservations.length === 0) {
    const tr = document.createElement("tr");
    tr.innerHTML = `<td colspan="5" style="text-align: center;">Aucune réservation n'est disponible.</td>`;
    tbody.appendChild(tr);
    return;
  }
  reservations.forEach((r) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
            <td>${r.id}</td>
            <td>${r.date_debut} <br>à ${r.date_fin}</td>
            <td><span style="padding:4px 8px; background:#e0e7ff; color:#4338ca; border-radius:4px; font-size:0.8rem">${r.status}</span></td>
            <td>Cli: ${r.client_id} / Ch: ${r.chambre_id}</td>
            <td><button class="btn-delete" data-id="${r.id}">X</button></td>
        `;
    tbody.appendChild(tr);
  });
}
