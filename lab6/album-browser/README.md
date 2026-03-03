# AlbumBrowser

An Angular SPA for browsing photo albums via the JSONPlaceholder REST API.  
Built for **Web Development — Lab 6: Routing & HTTP**.

## Features

- Multi-route SPA with Angular Router (6 routes)
- REST API integration using HttpClient & Observables
- CRUD operations: Read (list/detail), Update (edit title), Delete (remove)
- Service layer (`AlbumService`) — components never call HttpClient directly
- TypeScript interfaces for `Album` and `Photo` models
- Responsive photo grid with hover overlays
- Loading indicators on all async operations
- Dark, polished UI with Syne + DM Sans typography

## Routes

| Path | Component | Description |
|------|-----------|-------------|
| `/` | — | Redirects to `/home` |
| `/home` | HomeComponent | Welcome page |
| `/about` | AboutComponent | App info |
| `/albums` | AlbumsComponent | List all albums |
| `/albums/:id` | AlbumDetailComponent | Album detail + edit |
| `/albums/:id/photos` | AlbumPhotosComponent | Photo grid |

## Getting Started

### Prerequisites
- Node.js v18+ 
- Angular CLI v17+

```bash
npm install -g @angular/cli
```

### Install & Run

```bash
# Install dependencies
npm install

# Start dev server
ng serve

# Open in browser
# http://localhost:4200
```

### Build for Production

```bash
ng build
```

Output goes to `dist/album-browser/`.

## Project Structure

```
src/
└── app/
    ├── components/
    │   ├── home/
    │   ├── about/
    │   ├── albums/
    │   ├── album-detail/
    │   └── album-photos/
    ├── models/
    │   ├── album.model.ts
    │   └── photo.model.ts
    ├── services/
    │   └── album.service.ts
    ├── app.component.*
    ├── app.config.ts
    └── app.routes.ts
```

## API

Uses [JSONPlaceholder](https://jsonplaceholder.typicode.com) — a free fake REST API.

> Note: PUT/DELETE operations are simulated — changes won't persist on the server, but the UI updates locally.
