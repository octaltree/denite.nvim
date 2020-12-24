# ============================================================================
# FILE: converter/relative_word.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# License: MIT license
# ============================================================================

from os.path import isabs

from denite.base.filter import Base
from denite.util import relpath, Nvim, UserContext, Candidates


class Filter(Base):

    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)

        self.name = 'converter/relative_word'
        self.description = 'convert candidate word to relative path'

    def filter(self, context: UserContext) -> Candidates:
        for candidate in context['candidates']:
            if isabs(candidate['word']):
                candidate['word'] = relpath(
                    self.vim,
                    candidate.get('action__path', candidate['word']))
        return list(context['candidates'])
