# Have a Crack

Matt Bailey's phone web app: farm walks and runs (GPS map, GO/PAUSE/STOP, spots with photos and comments, share links, gold-medal ladder per walk), a boxing round timer, and recorded coach voices. Live at https://booga373.github.io/Have-a-crack/ (GitHub Pages, main branch, root). Family and farm visitors use it on their phones, no accounts.

## How to change it
- Edit `src/app.html` only, then run `python3 build.py`. It writes `index.html` (live site) and `dist/preview.html`, and fails if the script has a syntax error. Never hand-edit `index.html`.
- One self-contained page. External scripts only Leaflet 1.9.4 from cdnjs. Fonts from Google Fonts. No build tools, no frameworks.
- Data lives on each phone: walks in localStorage (`walkies.v1`), coach clips in IndexedDB (`hac`). Never rename these keys or change stored shapes without migrating, or people lose their walks and recordings.

## Things that must keep working (check before pushing)
- Big green GO, amber PAUSE, red STOP on both the walk recorder and the boxing timer.
- Time/Map toggle on the recorder; voice updates each km; "Come on, have a crack!" at the start of each boxing round; 10-second warning.
- Matt's Have a Crack picture as the logo and home-screen icon (`src/icon.jpg`).
- Settings: coach voice recording for walks and boxing, walk paces, map style.
- Share links (`#share=`) stay backward compatible with older links.
- Australian English, km and metres, plain friendly copy.
