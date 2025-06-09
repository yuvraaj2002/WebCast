llm_prompt = """
# ResearchCast: JSON Structured Research Paper-to-Podcast Conversion Prompt

## PRIMARY DIRECTIVE
Convert the provided research paper content into a natural two-person podcast conversation. Output must be in the exact JSON format specified below for easy programmatic processing and text-to-speech conversion. The podcast must comprehensively cover ALL research content including methodology, data analysis, mathematical formulas, tabular results, and conclusions without losing any information.

## REQUIRED JSON OUTPUT FORMAT

You MUST output your response as a valid JSON object in this exact structure:

```json
{
  "episode_metadata": {
    "title": "Episode Title Here",
    "paper_title": "Original Research Paper Title",
    "authors": "Author names from the paper",
    "duration_minutes": 35,
    "summary": "Brief episode summary describing the research findings and methodology covered",
    "research_domain": "Field of study (e.g., Machine Learning, Physics, Biology)"
  },
  "podcast_script": [
    {
      "speaker": "Speaker 1",
      "text": "Welcome to ResearchCast! Today we're breaking down this fascinating study..."
    },
    {
      "speaker": "Speaker 2", 
      "text": "I'm so excited to dive into these findings because..."
    },
    {
      "speaker": "Speaker 1",
      "text": "Let's start with the research question that motivated this work..."
    },
    {
      "speaker": "Speaker 2",
      "text": "That's such an important problem! Can you walk us through their methodology?"
    }
  ]
}
```

## SPEAKER ROLES

**Speaker 1**: The Research Expert
- Deep technical knowledge and expertise
- Explains complex methodologies and concepts
- Interprets data, formulas, and statistical results
- Provides context and significance of findings
- Handles technical details with authority

**Speaker 2**: The Inquisitive Analyst  
- Scientifically curious and analytically minded
- Asks probing questions about methodology and results
- Seeks clarification on technical aspects
- Challenges assumptions and explores implications
- Represents the perspective of someone with research background but not necessarily in this specific field

## RESEARCH CONTENT REQUIREMENTS

### COMPLETE PAPER COVERAGE - NO SUMMARIZATION ALLOWED
- **Abstract and Introduction**: Every detail of research motivation, problem statement, objectives, and background context
- **Literature Review**: ALL related work mentioned, every citation discussed, complete research gaps identified
- **Methodology**: EVERY step of experimental design, all data collection procedures, complete analytical approaches, every parameter and setting
- **Mathematical Formulas**: ALL equations must be explained in conversational language with complete derivations where provided
- **Tabular Data**: EVERY table must be discussed in complete detail - all rows, columns, values, comparisons, and statistical measures
- **Results**: ALL findings without exception, every statistical measure, all data interpretations, every experimental outcome
- **Discussion**: Complete implications, all limitations mentioned, every aspect of future work suggested
- **Conclusions**: All takeaways and every contribution to the field mentioned

### CRITICAL: ZERO INFORMATION LOSS POLICY
- Include EVERY piece of data, number, statistic, and measurement
- Mention ALL experimental conditions, parameters, and variables
- Discuss ALL figures, charts, graphs, and visual elements
- Reference ALL citations and related work mentioned
- Cover ALL mathematical proofs, derivations, and equations
- Present ALL results tables in complete detail
- Address ALL limitations, assumptions, and methodological choices
- Include ALL future work suggestions and research directions

### Mathematical Formula Handling - EXHAUSTIVE COVERAGE
When encountering formulas:
- Explain EVERY equation without exception
- Break down ALL complex formulas into every component
- Describe what EVERY variable, constant, and parameter represents
- Explain ALL mathematical relationships being expressed  
- Include ALL derivation steps if provided in the paper
- Connect ALL formulas to the broader research context
- Mention ALL assumptions and constraints for each equation

**Example Formula Discussion:**
```json
{
  "speaker": "Speaker 1",
  "text": "The core of their model relies on this key equation. Essentially, they're calculating the probability P of an event occurring, which equals the exponential of negative beta times the sum of weighted features, all divided by one plus that same exponential term."
},
{
  "speaker": "Speaker 2",
  "text": "So it's a logistic function! What makes their approach to weighting these features different from previous work?"
}
```

### Tabular Data Discussion - COMPLETE COVERAGE REQUIRED
For every table - NO EXCEPTIONS:
- Discuss EVERY row and column
- Mention ALL numerical values and measurements
- Compare ALL conditions, groups, and experimental settings
- Include ALL statistical measures (p-values, confidence intervals, standard deviations)
- Explain ALL trends, patterns, and anomalies in the data
- Reference ALL footnotes and table annotations

**Example Table Discussion - COMPREHENSIVE APPROACH:**
```json
{
  "speaker": "Speaker 1",
  "text": "Let's go through Table 2 completely - it shows their experimental results across all five datasets. For Dataset A, they achieved 94.7% accuracy with a standard deviation of 1.2%, compared to the baseline method which got 87.2% with 2.1% standard deviation. The p-value here is 0.001, showing statistical significance."
},
{
  "speaker": "Speaker 2",
  "text": "That's a 7.5 percentage point improvement with better consistency! What about the other datasets? I want to see every single result."
},
{
  "speaker": "Speaker 1",
  "text": "Absolutely! Dataset B showed 91.3% versus 88.7% baseline - that's 2.6% improvement. Dataset C had 89.1% versus 86.0% baseline - 3.1% gain. Dataset D achieved 93.8% versus 85.9% baseline - an impressive 7.9% improvement. And Dataset E got 90.4% versus 87.8% baseline - 2.6% gain. Every single comparison was statistically significant with p-values ranging from 0.001 to 0.03."
},
{
  "speaker": "Speaker 2",
  "text": "So we're seeing consistent improvements across all five datasets, with the magnitude varying from 2.6% to 7.9%. Were there any other metrics measured in this table?"
},
{
  "speaker": "Speaker 1",
  "text": "Yes! They also measured precision, recall, and F1-scores for each dataset. Let me go through all of those numbers as well..."
}
```

## DIALOGUE CREATION GUIDELINES

### Opening Pattern
```json
{
  "speaker": "Speaker 1",
  "text": "Welcome to ResearchCast! I'm absolutely fascinated by today's paper: [Paper Title]. This research tackles [main problem/question] in a completely novel way."
},
{
  "speaker": "Speaker 2",
  "text": "The results are impressive! What initially drew the researchers to this particular problem?"
},
{
  "speaker": "Speaker 1", 
  "text": "The motivation comes from [research gap/problem]. Let me walk you through what makes this work so significant..."
}
```

### Research Content Flow
1. **Problem Setup**: Research question, motivation, and significance
2. **Literature Context**: How this builds on previous work
3. **Methodology Deep Dive**: Experimental design and analytical approaches
4. **Mathematical Framework**: Key equations and their meaning
5. **Data Analysis**: Results from tables, figures, and statistical tests
6. **Interpretation**: What the findings mean and their implications
7. **Critical Analysis**: Limitations and future directions

### Technical Explanation Patterns
- **For Complex Concepts**: "Let me break this down step by step..."
- **For Formulas**: "This equation is telling us that..."
- **For Data**: "Looking at these numbers, what jumps out is..."
- **For Methods**: "Their approach works by..."
- **For Results**: "The key finding here is..."

### Question Patterns for Speaker 2
- "How does this methodology compare to [standard approach]?"
- "What do these numbers actually tell us?"
- "Is this result statistically significant?"
- "What are the practical implications of this finding?"
- "How robust is this conclusion?"
- "What assumptions are they making here?"
- "How might this change the field?"

## SPECIFIC RESEARCH PAPER INSTRUCTIONS

### Methodology Discussion
- Explain sample sizes, data sources, and collection methods
- Describe experimental conditions and controls
- Detail analytical techniques and statistical tests used
- Discuss validation approaches and robustness checks

### Results Interpretation
- Present findings clearly with numerical details
- Explain confidence intervals and p-values where relevant
- Compare results across different conditions
- Highlight unexpected or counterintuitive findings

### Critical Analysis
- Discuss limitations honestly
- Address potential biases or confounding factors
- Explore alternative explanations
- Consider generalizability of findings

### Future Implications
- Connect to broader research landscape
- Identify unanswered questions
- Suggest potential applications
- Discuss next steps for the field

## QUALITY REQUIREMENTS

### Research Completeness Checklist - EXHAUSTIVE COVERAGE
- [ ] Every single section of the paper is covered in complete detail
- [ ] ALL tables discussed with every data point mentioned
- [ ] ALL figures and charts explained completely
- [ ] Every mathematical formula explained without exception
- [ ] ALL methodology steps described in full detail
- [ ] Every statistical result and measure interpreted
- [ ] ALL experimental parameters and settings covered
- [ ] Every limitation and assumption addressed
- [ ] ALL future work suggestions included
- [ ] Every citation and reference mentioned
- [ ] Complete significance and implications discussed
- [ ] ALL appendices and supplementary material covered if present

### Technical Accuracy
- [ ] Mathematical concepts are correctly explained
- [ ] Statistical interpretations are accurate
- [ ] Technical terminology is used appropriately
- [ ] Complex ideas are made accessible without oversimplification

### Conversation Quality
- [ ] Natural, engaging scientific dialogue
- [ ] Appropriate level of technical detail
- [ ] Smooth transitions between research sections
- [ ] Genuine curiosity and analytical discussion
- [ ] Professional yet conversational tone

## CLOSING PATTERN
```json
{
  "speaker": "Speaker 2",
  "text": "This has been such a comprehensive look at this research. What do you think is the most significant contribution?"
},
{
  "speaker": "Speaker 1",
  "text": "[Key contribution and significance]. This work really pushes the field forward in [specific way]."
},
{
  "speaker": "Speaker 2",
  "text": "Absolutely! And the implications for [application area] could be tremendous. Any final thoughts on where this research might lead?"
},
{
  "speaker": "Speaker 1",
  "text": "I'm excited to see how other researchers build on these findings, especially in [specific direction]. Thanks for joining us for this deep dive into the research."
},
{
  "speaker": "Speaker 2",
  "text": "Thanks for walking us through such complex work so clearly. Until next time on ResearchCast!"
}
```

## JSON FORMAT REQUIREMENTS
- [ ] Valid JSON syntax with no errors
- [ ] Exact key names: "episode_metadata", "podcast_script"
- [ ] Metadata keys: "title", "paper_title", "authors", "duration_minutes", "summary", "research_domain"
- [ ] Script array with objects containing "speaker" and "text" keys
- [ ] Speaker values must be exactly "Speaker 1" or "Speaker 2"

## CRITICAL REMINDERS

1. **Output ONLY valid JSON** - no additional text before or after
2. **ZERO SUMMARIZATION** - include every single detail from the research paper
3. **Cover ALL research content** - methodology, data, formulas, tables, results, conclusions, references
4. **Explain every mathematical formula** in conversational terms with complete detail
5. **Discuss every table exhaustively** with all numbers, comparisons, and statistical measures
6. **Maintain scientific accuracy** while making content accessible
7. **Use exact key names** as specified in the format
8. **Ensure JSON syntax is perfect** - no trailing commas or syntax errors
9. **NO INFORMATION CAN BE LEFT OUT** - every piece of data must be discussed
10. **Include ALL experimental details** - parameters, settings, conditions, controls

## PROCESSING INSTRUCTIONS

1. Read and analyze the ENTIRE research paper content without skipping anything
2. Identify ALL sections: methodology, results, tables, formulas, conclusions, references, appendices
3. Plan the conversation flow covering ALL technical content in complete detail
4. Create explanations for EVERY mathematical formula in conversational language
5. Develop comprehensive table discussions covering ALL data points
6. Structure the JSON with complete metadata and exhaustive dialogue
7. Verify EVERY piece of research content is covered without any omission
8. Ensure JSON is valid and follows exact format specifications
9. **ABSOLUTELY NO SUMMARIZATION** - present everything in full detail
10. Double-check that no data, formula, table, or result has been skipped

---

**Now process the provided research paper content and output ONLY the JSON structured podcast dialogue following all specifications above. You must cover EVERY SINGLE aspect of the research including all methodology details, every mathematical formula, all tabular data with complete numbers, and all conclusions without losing ANY information whatsoever. Present everything in exhaustive detail - NO SUMMARIZATION ALLOWED. Do not include any text before or after the JSON.**
"""