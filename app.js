const API_URL = 'http://127.0.0.1:5000/api/notes';

// DOM Elements
const noteForm = document.getElementById('noteForm');
const noteTitle = document.getElementById('noteTitle');
const noteContent = document.getElementById('noteContent');
const errorMessage = document.getElementById('errorMessage');
const notesContainer = document.getElementById('notesContainer');
const searchInput = document.getElementById('searchInput');

// Global array to store notes for searching/filtering
let allNotes = [];

// 1. Fetch Notes on Page Load (READ)
async function fetchNotes() {
    try {
        const response = await fetch(API_URL);
        allNotes = await response.json();
        renderNotes(allNotes);
    } catch (error) {
        console.error("Error fetching notes:", error);
    }
}

// 2. Render Notes to the Screen
function renderNotes(notesToDisplay) {
    notesContainer.innerHTML = ''; // Clear container first

    notesToDisplay.forEach(note => {
        const card = document.createElement('div');
        card.className = 'note-card';

        card.innerHTML = `
            <h3>${note.title}</h3>
            <p>${note.content || 'No content'}</p>
            <button class="delete-btn" onclick="deleteNote(${note.id})">Delete</button>
        `;
        notesContainer.appendChild(card);
    });
}

// 3. Add a New Note (CREATE & Data Validation)
noteForm.addEventListener('submit', async (e) => {
    e.preventDefault(); // Stops the page from refreshing

    // DATA VALIDATION: Check if title is empty
    if (noteTitle.value.trim() === '') {
        errorMessage.classList.remove('hidden');
        return; // Stop execution
    } else {
        errorMessage.classList.add('hidden');
    }

    const newNote = {
        title: noteTitle.value,
        content: noteContent.value
    };

    try {
        await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(newNote)
        });

        // Clear form and refresh notes
        noteForm.reset();
        fetchNotes();
    } catch (error) {
        console.error("Error adding note:", error);
    }
});

// 4. Delete a Note (DELETE)
async function deleteNote(id) {
    try {
        await fetch(`${API_URL}/${id}`, {
            method: 'DELETE'
        });
        fetchNotes(); // Refresh the list after deleting
    } catch (error) {
        console.error("Error deleting note:", error);
    }
}

// 5. Search and Filter Feature
searchInput.addEventListener('input', (e) => {
    const searchTerm = e.target.value.toLowerCase();

    // Filter the global array based on the title
    const filteredNotes = allNotes.filter(note =>
        note.title.toLowerCase().includes(searchTerm)
    );

    renderNotes(filteredNotes);
});

// Load notes when the script starts
fetchNotes();