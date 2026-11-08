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
- Meditate: breathing patterns with the animated circle, guided sessions, quiet timer, background sounds (rain, ocean, wind, birdsong, binaural beats 6 Hz and 10 Hz for headphones), calm FEMALE guide voice, slow, soft and low with pauses between sentences and the background ducking under it (Matt asked for a calming lady's voice, not his), soft breath chimes on every phase change (rising = in, single = hold, falling = out) so people can breathe with eyes closed, shared mindful-minutes streak board.
- Share links (`#share=`) stay backward compatible with older links.
- Australian English, km and metres, plain friendly copy.

## Shared data (Supabase)
- Project https://ovmmhlvhplkgblncustm.supabase.co, public publishable key is in src/app.html (`DB`). Tables: `walks` (id, data jsonb, deleted), `results` (walk_id, who, ms), `clips` (coach voice rows); storage bucket `media` (photos/, people/, clips/).
- People profiles live in the `walks` table as rows with `data.kind = "person"` ({name, photo}). The walk list must always skip them.
- Meditation sessions are logged in the `results` table with walk_id `med:<session id>` (ms = time spent). Walk ladders must ignore them.
- Pictures used by the build: src/icon.jpg (logo/home-screen icon), src/tile-walk.jpg, src/tile-box.jpg (home tiles), src/avatar-matt.jpg (Matt's default profile picture), src/tile-med.jpg (Meditate tile: Matt meditating, calm colours), src/tile-new.jpg (Create a new walk tile: flexing on the farm). Tile pictures: walking and flexing on a farm background, boxing in a ring with RED gloves.
