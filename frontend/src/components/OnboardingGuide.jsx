/**
 * Onboarding guide component for displaying analysis results
 */

import React from 'react';
import {
  Box,
  Paper,
  Typography,
  Chip,
  Divider,
  Accordion,
  AccordionSummary,
  AccordionDetails,
  Alert,
} from '@mui/material';
import {
  ExpandMore as ExpandMoreIcon,
  CheckCircle as CheckCircleIcon,
  Info as InfoIcon,
} from '@mui/icons-material';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { useApp } from '../context/AppContext';

const OnboardingGuide = () => {
  const { repository, analysis } = useApp();

  if (!repository || !analysis) {
    return null;
  }

  return (
    <Paper elevation={3} sx={{ p: 3, mb: 3 }}>
      {/* Repository Header */}
      <Box sx={{ mb: 3 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
          <CheckCircleIcon color="success" />
          <Typography variant="h5" component="h2">
            {repository.name}
          </Typography>
        </Box>
        <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
          {repository.owner} • Branch: {repository.branch} • Commit: {repository.last_commit}
        </Typography>

        {/* Tech Stack */}
        {analysis.tech_stack && analysis.tech_stack.length > 0 && (
          <Box sx={{ display: 'flex', gap: 1, flexWrap: 'wrap' }}>
            {analysis.tech_stack.map((tech, index) => (
              <Chip key={index} label={tech} color="primary" size="small" />
            ))}
          </Box>
        )}
      </Box>

      <Divider sx={{ mb: 3 }} />

      {/* Overview */}
      {analysis.overview && (
        <Box sx={{ mb: 3 }}>
          <Typography variant="h6" gutterBottom sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
            <InfoIcon color="primary" />
            Project Overview
          </Typography>
          <Paper variant="outlined" sx={{ p: 2, bgcolor: 'grey.50' }}>
            <ReactMarkdown
              remarkPlugins={[remarkGfm]}
              components={{
                code({ node, inline, className, children, ...props }) {
                  const match = /language-(\w+)/.exec(className || '');
                  return !inline && match ? (
                    <SyntaxHighlighter
                      style={vscDarkPlus}
                      language={match[1]}
                      PreTag="div"
                      {...props}
                    >
                      {String(children).replace(/\n$/, '')}
                    </SyntaxHighlighter>
                  ) : (
                    <code className={className} {...props}>
                      {children}
                    </code>
                  );
                },
              }}
            >
              {analysis.overview}
            </ReactMarkdown>
          </Paper>
        </Box>
      )}

      {/* Setup Instructions */}
      {analysis.setup_instructions && (
        <Accordion defaultExpanded>
          <AccordionSummary expandIcon={<ExpandMoreIcon />}>
            <Typography variant="h6">Setup Instructions</Typography>
          </AccordionSummary>
          <AccordionDetails>
            <ReactMarkdown
              remarkPlugins={[remarkGfm]}
              components={{
                code({ node, inline, className, children, ...props }) {
                  const match = /language-(\w+)/.exec(className || '');
                  return !inline && match ? (
                    <SyntaxHighlighter
                      style={vscDarkPlus}
                      language={match[1]}
                      PreTag="div"
                      {...props}
                    >
                      {String(children).replace(/\n$/, '')}
                    </SyntaxHighlighter>
                  ) : (
                    <code className={className} {...props}>
                      {children}
                    </code>
                  );
                },
              }}
            >
              {analysis.setup_instructions}
            </ReactMarkdown>
          </AccordionDetails>
        </Accordion>
      )}

      {/* Architecture Insights */}
      {analysis.architecture_insights && (
        <Accordion>
          <AccordionSummary expandIcon={<ExpandMoreIcon />}>
            <Typography variant="h6">Architecture Insights</Typography>
          </AccordionSummary>
          <AccordionDetails>
            <ReactMarkdown
              remarkPlugins={[remarkGfm]}
              components={{
                code({ node, inline, className, children, ...props }) {
                  const match = /language-(\w+)/.exec(className || '');
                  return !inline && match ? (
                    <SyntaxHighlighter
                      style={vscDarkPlus}
                      language={match[1]}
                      PreTag="div"
                      {...props}
                    >
                      {String(children).replace(/\n$/, '')}
                    </SyntaxHighlighter>
                  ) : (
                    <code className={className} {...props}>
                      {children}
                    </code>
                  );
                },
              }}
            >
              {analysis.architecture_insights}
            </ReactMarkdown>
          </AccordionDetails>
        </Accordion>
      )}

      {/* Key Files */}
      {analysis.key_files && analysis.key_files.length > 0 && (
        <Accordion>
          <AccordionSummary expandIcon={<ExpandMoreIcon />}>
            <Typography variant="h6">Key Files ({analysis.key_files.length})</Typography>
          </AccordionSummary>
          <AccordionDetails>
            <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
              {analysis.key_files.map((file, index) => (
                <Paper key={index} variant="outlined" sx={{ p: 2 }}>
                  <Typography variant="subtitle2" sx={{ fontFamily: 'monospace', mb: 1 }}>
                    {file.path}
                  </Typography>
                  <Box sx={{ display: 'flex', gap: 1, mb: 1 }}>
                    <Chip label={file.type} size="small" />
                    {file.language && <Chip label={file.language} size="small" color="primary" />}
                    <Chip label={`${file.lines} lines`} size="small" variant="outlined" />
                  </Box>
                  {file.snippet && (
                    <SyntaxHighlighter
                      language={file.language || 'text'}
                      style={vscDarkPlus}
                      customStyle={{ fontSize: '0.75rem', maxHeight: '200px' }}
                    >
                      {file.snippet}
                    </SyntaxHighlighter>
                  )}
                </Paper>
              ))}
            </Box>
          </AccordionDetails>
        </Accordion>
      )}

      {/* Dependencies */}
      {analysis.dependencies && analysis.dependencies.length > 0 && (
        <Accordion>
          <AccordionSummary expandIcon={<ExpandMoreIcon />}>
            <Typography variant="h6">Dependencies</Typography>
          </AccordionSummary>
          <AccordionDetails>
            <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
              {analysis.dependencies.map((dep, index) => (
                <Box key={index}>
                  <Typography variant="subtitle2" sx={{ fontFamily: 'monospace', mb: 1 }}>
                    {dep.file}
                  </Typography>
                  <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
                    {Object.entries(dep.dependencies).slice(0, 20).map(([name, version]) => (
                      <Chip
                        key={name}
                        label={`${name}: ${version}`}
                        size="small"
                        variant="outlined"
                      />
                    ))}
                    {Object.keys(dep.dependencies).length > 20 && (
                      <Chip
                        label={`+${Object.keys(dep.dependencies).length - 20} more`}
                        size="small"
                        variant="outlined"
                      />
                    )}
                  </Box>
                </Box>
              ))}
            </Box>
          </AccordionDetails>
        </Accordion>
      )}

      <Alert severity="info" sx={{ mt: 3 }}>
        <Typography variant="body2">
          <strong>Ready to explore?</strong> Use the chat interface below to ask questions about this codebase!
        </Typography>
      </Alert>
    </Paper>
  );
};

export default OnboardingGuide;

// Made with Bob
