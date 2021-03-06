
from resumable.files import ResumableFile as OrigResumableFile


class ResumableFile(OrigResumableFile):
    def chunk_names(self):
        """Iterates over all stored chunks and yields their names."""
        file_names = sorted(self.storage.listdir('')[1])
        pattern = '%s%s' % (self.filename, self.chunk_suffix)
        for name in file_names:
            if name[:-4] == pattern:
                yield name
