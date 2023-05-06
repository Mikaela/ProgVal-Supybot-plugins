###
# Copyright (c) 2010, quantumlemur
# Copyright (c) 2011, Valentin Lorentz
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

from supybot.test import *
import supybot.conf as conf

class WikipediaTestCase(PluginTestCase):
    plugins = ('Wikipedia',)

    if network:
        def testWiki(self):
            self.assertRegexp('wiki Monty Python',
                              '^Monty Python \(.* known as The Pythons\).*')

        def testWikiDisambiguation(self):
            self.assertRegexp('wiki Python', 'Python may refer to: Snakes.*')

        def testWikiRedirect(self):
            self.assertRegexp(
                'wiki Foo',
                r'^"Foobar" \(Redirected from "Foo"\): The terms foobar.*')
            with conf.supybot.plugins.Wikipedia.showRedirects.context(False):
                self.assertRegexp(
                    'wiki Foo',
                    r'^The terms foobar.*')

        def testRedirect2(self):
            self.assertRegexp(
                'wiki The Pythons',
                r'^"Monty Python" \(Redirected from "The Pythons"\): '
                r'Monty Python \(.* known as The Pythons\).*')

        def testWikiNotFound(self):
            self.assertRegexp('wiki roegdfjpoepo',
                              'Not found, or page malformed.*')

        def testStripInlineCitations(self):
            self.assertNotRegexp('wiki UNICEF', '\[\d+\]')

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
