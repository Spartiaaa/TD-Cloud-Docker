import * as API from "./api.js";
import { API_BASE_URL } from "./config.js";

/* ====================================================================
   0. SÉLECTEURS GLOBALS & FONCTIONS UTILITAIRES (CHAMBRES)
==================================================================== */
// Sélecteurs pour le module CHAMBRES (utilisés seulement si l'élément existe sur la page)
const chambreForm = document.getElementById("chambre-form");
const chambreIdField = document.getElementById("chambre_id");
const formTitle = document.getElementById("form-title");
const submitBtn = document.getElementById("submit-btn");
const cancelBtn = document.getElementById("cancel-btn");
const listTitle = document.getElementById("list-title");
const tableBodyChambres = document.getElementById("table-body-chambres");
const filterForm = document.getElementById("filter-form");

// --- Fonctions d'interface CHAMBRES ---

/** Réinitialise le formulaire de création/édition de chambre. */
const resetChambreForm = function () {
  chambreForm?.reset();
  if (chambreIdField) chambreIdField.value = "";
  if (formTitle) formTitle.textContent = "Ajouter une Chambre";
  if (submitBtn) submitBtn.textContent = "Enregistrer";
  if (cancelBtn) cancelBtn.style.display = "none";
  const hotelIdInput = document.getElementById("hotel_id");
  if (hotelIdInput) hotelIdInput.disabled = false;
};
if (cancelBtn) {
  cancelBtn.addEventListener("click", () => resetChambreForm());
}

/** Rempli le formulaire d'édition avec les données d'une chambre sélectionnée. */
const handleEditChambre = function (id, trElement) {
  const chambreData = {
    id: id,
    // Indices des colonnes : ID(0), Numéro(1), Type(2), Prix(3), État(4), Hôtel(5), Action(6)
    numero: parseInt(trElement.children[1].textContent),
    type: trElement.children[2].textContent,
    prix: parseFloat(trElement.children[3].textContent.replace(" €", "")),
    etat: trElement.children[4].textContent.trim(),
    hotel_id: parseInt(trElement.children[5].textContent.replace("#", "")),
  };

  if (chambreIdField) chambreIdField.value = chambreData.id;
  if (document.getElementById("numero"))
    document.getElementById("numero").value = chambreData.numero;
  if (document.getElementById("type"))
    document.getElementById("type").value = chambreData.type;
  if (document.getElementById("prix"))
    document.getElementById("prix").value = chambreData.prix;
  if (document.getElementById("etat"))
    document.getElementById("etat").value = chambreData.etat;
  if (document.getElementById("hotel_id"))
    document.getElementById("hotel_id").value = chambreData.hotel_id;

  if (document.getElementById("hotel_id"))
    document.getElementById("hotel_id").disabled = true;

  if (formTitle)
    formTitle.textContent = `Modifier la Chambre #${chambreData.id}`;
  if (submitBtn) submitBtn.textContent = "Mettre à jour";
  if (cancelBtn) cancelBtn.style.display = "inline-block";
  window.scrollTo({ top: 0, behavior: "smooth" });
};

/** Affiche les chambres dans le tableau HTML. */
const renderChambresTable = function (chambres, hotelId) {
  if (listTitle) listTitle.textContent = `Chambres de l'Hôtel #${hotelId}`;
  if (!tableBodyChambres) return;

  tableBodyChambres.innerHTML = "";
  if (chambres.length === 0) {
    tableBodyChambres.innerHTML = `<tr><td colspan="7" style="text-align: center;">Aucune chambre trouvée pour cet hôtel.</td></tr>`;
    return;
  }

  chambres.forEach((chambre) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
            <td>${chambre.id}</td>
            <td><strong>${chambre.numero}</strong></td>
            <td>${chambre.type}</td>
            <td>${chambre.prix} €</td>
            <td>${chambre.etat} </td>
            <td>#${chambre.hotel_id}</td>
            <td>
                <button class="btn-secondary btn-edit" data-id="${chambre.id}">
                    Éditer
                </button>
            </td>
        `;
    tableBodyChambres.appendChild(tr);
  });
};

/* ====================================================================
   1. CHARGEMENT GLOBAL
==================================================================== */
document.addEventListener("DOMContentLoaded", () => {
  // Les fonctions de chargement des autres entités sont appelées ici.
  loadHotels();
  loadClients();
  loadReservations();

  // Initialisation du filtre de chambre (uniquement si le champ existe sur la page)
  const initialHotelId = 1;
  const filterInput = document.getElementById("filter_hotel_id");

  if (filterInput) {
    filterInput.value = initialHotelId;
    loadChambres(initialHotelId);
  }
});

/* ====================================================================
   2. HÔTELS 🏨
==================================================================== */

/** Affiche la liste des hôtels dans le tableau (utilisé par loadHotels). */
const renderHotelsTable = (hotels) => {
  const tbody = document.getElementById("table-body-hotels");
  if (!tbody) return;
  tbody.innerHTML = "";

  if (hotels.length === 0) {
    // Colspan mis à 3 (ID, Nom, Adresse)
    tbody.innerHTML = `<tr><td colspan="3" style="text-align: center;">Aucun hôtel trouvé.</td></tr>`;
    return;
  }

  hotels.forEach((h) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
            <td><strong>#${h.id}</strong></td>
            <td>${h.nom}</td>
            <td>${h.adresse}</td>
            `;
    tbody.appendChild(tr);
  });
};

async function loadHotels() {
  try {
    const hotels = await API.getHotels();
    renderHotelsTable(hotels);
  } catch (err) {
    alert(
      "Erreur chargement hôtels : " +
        (err.message || "Impossible de joindre l'API."),
    );
  }
}

document.getElementById("hotel-form")?.addEventListener("submit", async (e) => {
  e.preventDefault();
  const data = {
    nom: document.getElementById("nom").value,
    adresse: document.getElementById("adresse").value,
  };
  try {
    await API.createHotel(data);
    e.target.reset();
    loadHotels();
  } catch (err) {
    alert("Erreur création hôtel : " + err.message);
  }
});
// NOTE: Le gestionnaire de suppression a été retiré (API DELETE non implémentée pour Hôtels).

/* ====================================================================
   3. CHAMBRES 🛏️
==================================================================== */

export async function loadChambres(hotelId) {
  if (!hotelId) {
    console.warn("loadChambres: ID d'hôtel manquant.");
    renderChambresTable([], 0);
    return;
  }
  try {
    const chambres = await API.getChambresByHotel(hotelId);
    renderChambresTable(chambres, hotelId);
  } catch (err) {
    console.error("Erreur chargement chambres:", err);
    alert(
      `Erreur chargement chambres pour l'Hôtel #${hotelId} : ` +
        (err.message || "Erreur de connexion."),
    );
    renderChambresTable([], hotelId);
  }
}

filterForm?.addEventListener("submit", (e) => {
  e.preventDefault();
  const hotelId = parseInt(document.getElementById("filter_hotel_id").value);
  if (!isNaN(hotelId) && hotelId > 0) {
    loadChambres(hotelId);
  } else {
    alert("Veuillez entrer un ID d'hôtel valide.");
  }
});

chambreForm?.addEventListener("submit", async (e) => {
  e.preventDefault();

  const chambreId = document.getElementById("chambre_id")?.value;
  const isEditing = !!chambreId;

  const data = {
    numero: parseInt(document.getElementById("numero").value),
    type: document.getElementById("type").value,
    prix: parseFloat(document.getElementById("prix").value),
    etat: document.getElementById("etat").value,
    hotel_id: parseInt(document.getElementById("hotel_id").value),
  };

  if (isNaN(data.numero) || isNaN(data.prix) || isNaN(data.hotel_id)) {
    alert("Veuillez vérifier les numéros et prix (nombre requis).");
    return;
  }

  try {
    if (isEditing) {
      await API.updateChambre(chambreId, data);
      alert(`Chambre #${chambreId} mise à jour avec succès.`);
    } else {
      await API.createChambre(data);
      alert("Chambre créée avec succès.");
    }

    resetChambreForm();
    const currentHotelId = document.getElementById("filter_hotel_id")?.value;
    if (currentHotelId) {
      loadChambres(parseInt(currentHotelId));
    }
  } catch (err) {
    alert(
      `Erreur ${isEditing ? "mise à jour" : "création"} chambre : ` +
        err.message,
    );
  }
});

tableBodyChambres?.addEventListener("click", async (e) => {
  const id = e.target.dataset.id;

  if (e.target.classList.contains("btn-edit")) {
    handleEditChambre(id, e.target.closest("tr"));
  }
});

/* ====================================================================
   4. CLIENTS 👤
==================================================================== */
const renderClientsTable = (clients) => {
  const tbody = document.getElementById("table-body-clients");
  if (!tbody) return;
  tbody.innerHTML = "";

  if (clients.length === 0) {
    // Colspan mis à 4 (ID, Nom, Email, Téléphone)
    tbody.innerHTML = `<tr><td colspan="4" style="text-align: center;">Aucun client trouvé.</td></tr>`;
    return;
  }

  clients.forEach((c) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
            <td><strong>#${c.id}</strong></td>
            <td>${c.nom}</td>
            <td>${c.email}</td>
            <td>${c.tel || ""}</td>
            `;
    tbody.appendChild(tr);
  });
};

async function loadClients() {
  try {
    const clients = await API.getClients();
    renderClientsTable(clients);
  } catch (err) {
    alert(
      "Erreur chargement clients : " +
        (err.message || "Impossible de joindre l'API."),
    );
  }
}

document
  .getElementById("client-form")
  ?.addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = {
      nom: document.getElementById("nom").value,
      email: document.getElementById("email").value,
      tel: document.getElementById("tel").value,
    };

    try {
      await API.createClient(data);
      e.target.reset();
      loadClients();
    } catch (err) {
      alert("Erreur création client : " + err.message);
    }
  });
// NOTE: Le gestionnaire de suppression a été retiré (API DELETE non implémentée pour Clients).

/* ====================================================================
   5. RÉSERVATIONS 📅
==================================================================== */
const renderReservationsTable = (reservations) => {
  const tbody = document.getElementById("table-body-reservations");
  if (!tbody) return;
  tbody.innerHTML = "";

  if (reservations.length === 0) {
    tbody.innerHTML = `<tr><td colspan="5" style="text-align: center;">Aucune réservation trouvée.</td></tr>`;
    return;
  }

  reservations.forEach((r) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
            <td>${r.id}</td>
            <td>${r.date_debut} <br>à ${r.date_fin}</td>
            <td><span style="padding:4px 8px; background:#e0e7ff; color:#4338ca; border-radius:4px; font-size:0.8rem">${r.status}</span></td>
            <td>Cli: ${r.client_id} / Ch: ${r.chambre_id}</td>
            <td><button class="btn-danger btn-delete" data-id="${r.id}">X</button></td>
        `;
    tbody.appendChild(tr);
  });
};

async function loadReservations() {
  try {
    const reservations = await API.getReservations();
    renderReservationsTable(reservations);
  } catch (err) {
    alert(
      "Erreur chargement réservations : " +
        (err.message || "Impossible de joindre l'API."),
    );
  }
}

document
  .getElementById("reservation-form")
  ?.addEventListener("submit", async (e) => {
    e.preventDefault();

    const client_id_val = parseInt(document.getElementById("client_id").value);
    const chambre_id_val = parseInt(
      document.getElementById("chambre_id").value,
    );

    if (isNaN(client_id_val) || isNaN(chambre_id_val)) {
      alert(
        "Erreur: Les ID Client et ID Chambre doivent être des nombres entiers valides.",
      );
      return;
    }

    const data = {
      date_debut: document.getElementById("date_debut").value,
      date_fin: document.getElementById("date_fin").value,
      status: document.getElementById("status").value,
      client_id: client_id_val,
      chambre_id: chambre_id_val,
    };

    try {
      await API.createReservation(data);
      alert("Réservation créée avec succès !");
      e.target.reset();
      loadReservations();
    } catch (err) {
      let errorMessage =
        "Erreur lors de la réservation. Veuillez vérifier les IDs et réessayer.";
      const errorDetail = err.message || "";

      if (
        errorDetail.includes("a foreign key constraint fails") ||
        errorDetail.includes("1452")
      ) {
        errorMessage =
          "Erreur de contrainte : L'ID de la Chambre et/ou l'ID du Client n'existent pas dans la base de données.";
      } else if (errorDetail.includes("Erreur 422")) {
        errorMessage =
          "Erreur de validation : Certains champs sont manquants ou invalides.";
      }

      console.error("Erreur POST Réservation:", err);
      alert(errorMessage);
    }
  });

document
  .getElementById("table-body-reservations")
  ?.addEventListener("click", async (e) => {
    if (
      e.target.classList.contains("btn-delete") &&
      confirm("Supprimer cette réservation ?")
    ) {
      try {
        await API.deleteReservation(e.target.dataset.id);
        loadReservations();
      } catch (err) {
        alert(
          "Erreur suppression réservation: " +
            (err.message || "Échec de l'opération."),
        );
      }
    }
  });
