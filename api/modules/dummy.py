from typing import Any, Generator
import time

DUMMY_DATA = """
The old lighthouse keeper, Silas, was a man of few words, and fewer teeth. For seventy years, he’d lived on the lonely island, his only companions the gulls and the rhythmic pulse of the lamp. His face was etched with wrinkles that mirrored the waves crashing against the jagged rocks below.

One blustery evening, a small boat, battered and bruised by a sudden storm, limped towards the island. Silas, squinting through the swirling rain, saw a young woman clinging to the mast. She was small, no older than twenty, with hair the color of sea foam and eyes wide with fear.

He hauled her onto the island, his gnarled hands surprisingly strong. He brought her to the cozy warmth of the lighthouse, a haven of oil lamps and the comforting scent of beeswax. She introduced herself as Elara, a marine biologist chasing a rare species of bioluminescent jellyfish.

For days, the storm raged, keeping Elara and Silas confined to the lighthouse. They were an unlikely pair, separated by generations and worlds. He told her stories of shipwrecks and close calls, his voice a low rumble that competed with the howling wind. She, in turn, told him about the mysteries of the deep, about creatures that glowed with their own light, about the delicate balance of life beneath the waves.

He learned to appreciate the wonder in her eyes, the passion that burned within her. She learned to see past the gruff exterior of the old man, to recognize the quiet strength and the profound respect he held for the sea.

Finally, the storm passed. As Elara prepared to leave, she hesitated at the doorway, the morning sun painting the sea in hues of gold and rose.

“Thank you, Silas,” she said, her voice thick with emotion. “For everything.”

He just nodded, his eyes, usually shielded by the perpetual squint, suddenly clear and bright.

“Safe travels,” he rasped, his voice a little thicker than usual.

Elara boarded a passing fishing boat and sailed away, leaving Silas alone once more with the gulls and the lamp. But something had changed. The lighthouse, once just a lonely sentinel, now held the memory of shared stories, of unexpected connection, of a light that shone brighter than any beacon. And Silas, the old lighthouse keeper, knew that even on a lonely island, the human heart could still find a harbor.

"""


def dummy_generator() -> Generator[str | None, Any, Any]:
  for line in DUMMY_DATA.split("\n"):
    time.sleep(0.3)
    yield line
