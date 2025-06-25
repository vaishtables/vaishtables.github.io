(async function () {
  const [style, locale, bibData] = await Promise.all([
    fetch('theme/js/chicago.csl').then(r => r.text()),
    fetch('theme/js/locales-en-US.xml').then(r => r.text()),
    fetch('theme/js/Personal.json').then(r => r.json())
  ]);

  const bib = Array.isArray(bibData)
    ? Object.fromEntries(bibData.map(entry => [entry.id, entry]))
    : bibData;

  console.log("Available bib keys:", Object.keys(bib));

  const sys = {
    retrieveLocale: () => locale,
    retrieveItem: id => {
      if (!bib[id]) {
        console.warn(`Missing citation item for ID: ${id}`);
      }
      return bib[id];
    }
  };

  const citeproc = new CSL.Engine(sys, style);
  const spans = Array.from(document.querySelectorAll("span[data-citationitems]"));
  const citationHistory = [];

  for (let span of spans) {
    const citationID = span.id;
    const keys = JSON.parse(span.getAttribute("data-citationitems"));
    const citationItems = keys.map(id => ({ id }));
    const citation = {
      citationID,
      citationItems,
      properties: {
        noteIndex: 0,
        ...(citationID.startsWith('NAR') ? { mode: 'composite' } : {})
      }
    };

    const citationsPre = citationHistory.map(c => [c.citationID, 0]);
    const result = citeproc.processCitationCluster(citation, citationsPre, []);
    citationHistory.push({ citationID });

    if (result[1] && result[1][0]) {
      span.textContent = result[1][0][1];
    }
  }

  // Generate bibliography after all citations are processed
  const [bibMeta, bibEntries] = citeproc.makeBibliography();

  // Compose the full bibliography HTML string
  const bibliographyHTML = 
    '<hr>' + 
    bibMeta.bibstart + 
    bibEntries.join('') + 
    bibMeta.bibend;

  // Append the bibliography to the document body or a specific container
  const bibContainer = document.createElement('div');
  bibContainer.id = 'bibliography';
  bibContainer.innerHTML = bibliographyHTML;

  document.body.appendChild(bibContainer);
})();
