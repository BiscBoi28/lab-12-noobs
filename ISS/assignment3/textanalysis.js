const pronouns = ['i', 'me', 'my', 'mine', 'you', 'your', 'yours', 'he', 'him', 'his', 'she', 'her', 'hers', 'it', 'its', 'we', 'us', 'our', 'ours', 'they', 'them', 'their', 'theirs', 'who', 'whom', 'whose', 'which', 'that', 'this', 'that', 'these', 'those'];

const prepositions = ['about', 'above', 'across', 'after', 'against', 'along', 'amid', 'among', 'around', 'at', 'before', 'behind', 'below', 'beneath', 'beside', 'between', 'beyond', 'by', 'down', 'during', 'except', 'for', 'from', 'in', 'into', 'like', 'near', 'of', 'off', 'on', 'onto', 'out', 'over', 'past', 'since', 'through', 'to', 'toward', 'under', 'until', 'up', 'upon', 'with', 'within', 'without'];

const indefiniteArticles = ['a', 'an'];

function analyzeText() {
    const text = document.getElementById('textInput').value;
    let output = '';
    
    // Basic counts
    const letters = (text.match(/[a-zA-Z]/g) || []).length;
    const words = text.trim().split(/\s+/).length;
    const spaces = (text.match(/\s/g) || []).length;
    const newlines = (text.match(/\n/g) || []).length;
    const specialSymbols = (text.match(/[^a-zA-Z0-9\s]/g) || []).length;

    // Tokenize text
    const words_array = text.toLowerCase().match(/\b\w+\b/g) || [];

    // Check for pronouns
    let foundPronouns = false;
    const pronounCounts = pronouns.map(pronoun => {
        const count = words_array.filter(word => word === pronoun).length;
        if (count > 0) {
            foundPronouns = true;
            return `${pronoun}: ${count}`;
        }
        return '';
    }).filter(line => line);

    // Check for prepositions
    let foundPrepositions = false;
    const prepositionCounts = prepositions.map(prep => {
        const count = words_array.filter(word => word === prep).length;
        if (count > 0) {
            foundPrepositions = true;
            return `${prep}: ${count}`;
        }
        return '';
    }).filter(line => line);

    // Check for indefinite articles
    let foundArticles = false;
    const articleCounts = indefiniteArticles.map(article => {
        const count = words_array.filter(word => word === article).length;
        if (count > 0) {
            foundArticles = true;
            return `${article}: ${count}`;
        }
        return '';
    }).filter(line => line);

    output = `<div class="result-section">
        <div class="result-heading">Basic Analysis:</div>
        Letters: ${letters}
        Words: ${words}
        Spaces: ${spaces}
        Newlines: ${newlines}
        Special Symbols: ${specialSymbols}
    </div>

    <div class="result-section">
        <div class="result-heading">Pronouns:</div>
        ${foundPronouns ? pronounCounts.join('\n') : 'No pronouns found in the text.'}
    </div>

    <div class="result-section">
        <div class="result-heading">Prepositions:</div>
        ${foundPrepositions ? prepositionCounts.join('\n') : 'No prepositions found in the text.'}
    </div>

    <div class="result-section">
        <div class="result-heading">Indefinite Articles:</div>
        ${foundArticles ? articleCounts.join('\n') : 'No indefinite articles found in the text.'}
    </div>`;

    document.getElementById('results').innerHTML = output;
}