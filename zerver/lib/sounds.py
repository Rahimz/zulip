import os

from zerver.lib.storage import static_path


def get_available_notification_sounds() -> list[str]:
    notification_sounds_path = static_path("audio/notification_sounds")
    available_notification_sounds = []

    for file_name in os.listdir(notification_sounds_path):
        root, ext = os.path.splitext(file_name)
        if "." in root:  # nocoverage
            # Exclude e.g. zulip.abcd1234.ogg (generated by production hash-naming)
            # to avoid spurious duplicates.
            continue
        if ext == ".ogg":
            available_notification_sounds.append(root)

    return sorted(available_notification_sounds)
