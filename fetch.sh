#!/bin/bash
leetcode-export --folder submissions --problem-statement-content '# [${question_id} - ${title}](https://leetcode.com/problems/${title_slug}/) </br> Difficulty: ${difficulty}' --problem-statement-filename "readme.md" --only-accepted --submission-filename '${date_formatted} - ${lang} - runtime ${runtime} - memory ${memory}.${extension}'