# Private Markets Investment Control Matrix - UI Prototype

This repository contains the complete UI documentation and interactive prototype for the Private Markets Investment Control Matrix system.

## Overview

The PMICM is a comprehensive platform for allocators to manage capital calls, monitor distributions, track fees, and reconcile data against General Partner (GP) reports.

## Screens

### 1. **Dashboard**
   - Quick view of all exceptions by type and severity
   - Summary cards showing counts
   - Filterable exception table
   - Access point for all user workflows

### 2. **Exception Review**
   - Detailed view of a specific discrepancy
   - Expected vs Actual comparison
   - Embedded document viewer with extracted fields
   - Approval/rejection actions with full audit trail

### 3. **Document Viewer + Extraction**
   - PDF viewer with highlighting
   - Extracted fields shown in sidebar with confidence scores
   - Provenance controls to link back to source documents
   - Read-only transparency view

### 4. **LPA / Side Letter Canonicalization**
   - Structured representation of fund agreements
   - Clause-by-clause breakdown
   - Investor-specific modeling
   - Expected behavior computation

### 5. **Reconciliation**
   - Variance comparison table (GP vs Expected vs Allocator)
   - Trend charts for variance, commitment, and fees
   - Drill-down to specific exceptions
   - Bulk resolution actions

### 6. **Approval Workflow**
   - Task assignment and tracking
   - Timeline view of exception progression
   - Complete audit trail with timestamps and user info
   - Version history of decisions

### 7. **Settings / Integrations**
   - Connect accounting systems (Allvue, Juniper Square, QuickBooks, Sage, Snowflake)
   - API key and webhook management
   - User roles and permissions (Admin, Reviewer, Viewer)
   - SSO / SAML configuration

## User Flows

### Flow 1: Daily Exception Triage
1. User lands on Dashboard
2. Reviews exception cards and filters table
3. Clicks exception → Exception Review
4. Makes approval decision → Status updates
5. Exception appears in Approval Workflow

### Flow 2: Document-Based Investigation
1. From Exception Review, opens Document Viewer
2. Reviews extracted fields and provenance
3. Toggles to LPA Modeling if terms need adjustment
4. Recalculates expected values
5. Returns to Exception Review to finalize decision

### Flow 3: Periodic Reconciliation
1. User opens Reconciliation screen
2. Reviews variance table and charts
3. Filters by fund, GP, date range
4. Drills into specific variances
5. Marks as resolved or escalates

### Flow 4: Setup & Integrations
1. Admin opens Settings
2. Connects accounting and portfolio systems
3. Configures roles and permissions
4. Enables SSO

## Components

- **Top Bar**: Logo, fund selector, search, user profile
- **Exception Cards**: Summary counts by type and severity
- **Exception Table**: Sortable, filterable list of exceptions
- **PDF Viewer**: Embedded document viewer with zoom and thumbnails
- **Extraction Sidebar**: Structured fields with confidence scores
- **Clause Viewer**: Raw and structured clause representation
- **Variance Table**: GP vs Expected vs Allocator comparison
- **Timeline**: Workflow progression with audit trail
- **Integration List**: System connection status and config

## Color Scheme

- **High Severity**: #dc3545 (Red)
- **Medium Severity**: #ff9800 (Orange)
- **Low Severity**: #4caf50 (Green)
- **Primary Action**: #0066cc (Blue)
- **Success/Approved**: #4caf50 (Green)
- **Error/Rejected**: #dc3545 (Red)

## How to View the Prototype

1. Navigate to `ui/prototype.html` in this repository
2. Open in a web browser
3. Use the navigation tabs to switch between screens
4. Click "Review" buttons to navigate to Exception Review
5. All screens are interactive and demonstrate the full user experience

## File Structure

```
ui/
├── components.md          # UI components and states
├── flows.md              # User workflows
├── prototype.html        # Interactive HTML prototype
└── screens/
    ├── dashboard.md      # Dashboard screen spec
    ├── exception_review.md
    ├── document_viewer.md
    ├── lpa_modeling.md
    ├── reconciliation.md
    ├── approvals.md
    └── settings.md
```

## Next Steps

1. **Design System**: Expand prototype with Figma design tokens
2. **API Integration**: Connect to backend services
3. **Testing**: User acceptance testing with allocators
4. **Mobile**: Responsive design for mobile/tablet
5. **Accessibility**: WCAG 2.1 compliance enhancements

