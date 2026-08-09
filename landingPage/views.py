from django.shortcuts import render, get_object_or_404
from django.http import Http404


# Service data - in a real project this would be in the database
SERVICES = {
    'loan-servicing-call-center': {
        'title': 'Loan Servicing Call Center',
        'subtitle': 'Clear Communication. Reduced Friction. Stronger Borrower Confidence.',
        'image': 'images/loan-servicing-call-center.png',
        'intro': [
            'Our loan servicing call center supports inbound borrower interactions with clarity, professionalism, and structured documentation.',
            'Loan servicing communication often determines how borrowers perceive your organization. Confusion, delayed responses, or inconsistent messaging can increase dissatisfaction and escalate complaints.',
        ],
        'sections': [
            {
                'heading': 'TELEPRO ensures that each borrower interaction is managed with:',
                'items': ['Active listening', 'Empathetic communication', 'Accurate information delivery', 'Clear next-step guidance', 'Structured documentation'],
            },
            {
                'heading': 'Our servicing support includes:',
                'items': ['Account balance inquiries', 'Payment due-date clarification', 'Payment processing assistance', 'Renewal and extension guidance', 'Hardship communication', 'Document clarification and follow-ups', 'Account updates and changes'],
            },
        ],
        'closing': [
            'All interactions are logged within your Loan Management System (LMS) and CRM platforms, ensuring full transparency and internal visibility.',
            'Our goal is not just to resolve calls — it is to reinforce borrower understanding and reduce repeat contact rates.',
        ],
        'cta_line': "Let's enhance your customer support strategy.",
    },
    'collections-call-center-for-lenders': {
        'title': 'Collections Call Center for Lenders',
        'subtitle': 'Performance-Driven. Respectful. Structured.',
        'image': 'images/collections-call-center-for-lenders.png',
        'intro': [
            'Collections communication is one of the most sensitive aspects of lending operations. Borrowers experiencing financial stress require professional, empathetic, and structured engagement.',
            'Our collections call center services are designed to improve repayment performance while maintaining borrower dignity and brand integrity.',
        ],
        'sections': [
            {
                'heading': 'We support:',
                'items': ['Early-stage delinquency outreach', 'Mid-stage recovery follow-ups', 'Promise-to-pay tracking and follow-up', 'Retention-focused repayment discussions', 'Escalation routing for complex cases', 'Renewal re-engagement conversations'],
            },
            {
                'heading': 'Our structured collections framework focuses on:',
                'items': ['Clear communication of obligations', 'Documentation accuracy', 'Professional tone', 'Measurable performance metrics', 'Transparent reporting'],
            },
            {
                'heading': 'We monitor key performance indicators including:',
                'items': ['Promise-to-Pay (PTP) conversion rates', 'Right-party contact rates', 'Call quality scoring', 'Escalation patterns', 'Repayment engagement trends'],
            },
        ],
        'closing': [
            'Collections is not about pressure — it is about disciplined communication aligned with performance goals.',
        ],
        'cta_line': "Let's enhance your customer support strategy.",
    },
    'inbound-outbound-call-handling': {
        'title': 'Inbound & Outbound Call Handling',
        'subtitle': 'Professional Borrower Engagement Across Every Touchpoint',
        'image': 'images/inbound-outbound-call-handling.png',
        'intro': [
            'TELEPRO provides comprehensive inbound and outbound call handling tailored specifically to lending environments.',
            'Effective communication is at the heart of every successful customer relationship. Our Inbound and Outbound Call Handling services are designed to ensure that every interaction with your customers is smooth, professional, and impactful—whether they\'re reaching out to you or you\'re connecting with them.',
        ],
        'sections': [
            {
                'title': 'Inbound Call Handling',
                'description': 'Inbound communication requires patience, clarity, and efficiency. Our inbound specialists are trained to handle:',
                'heading': 'Key Features:',
                'items': ['Product inquiries', 'Account questions', 'Technical servicing support', 'Billing clarification', 'Complaint intake and resolution', 'General borrower support'],
                'after': 'We prioritize first-call resolution whenever possible while maintaining structured escalation pathways when necessary.',
            },
            {
                'title': 'Outbound Call Handling',
                'description': 'Outbound engagement is essential for repayment reinforcement, renewal outreach, and lead qualification.',
                'heading': 'Our outbound capabilities include:',
                'items': ['Lead follow-ups', 'Application completion reminders', 'Renewal campaigns', 'Payment reminder outreach', 'Delinquency follow-ups', 'Reactivation programs'],
            },
            {
                'heading': 'Each campaign is supported by:',
                'items': ['Script customization aligned with your brand voice', 'KPI-based performance tracking', 'Documented follow-through', 'Outcome reporting transparency'],
            },
        ],
        'closing': [
            'Outbound communication is structured around measurable results — not just call volume.',
        ],
        'cta_line': "Let's talk about how we can support your business.",
    },
    'live-chat-support': {
        'title': 'Live Chat Support',
        'subtitle': 'Real-Time Digital Engagement for Modern Borrowers',
        'image': 'images/live-chat-email-support.png',
        'intro': [
            'Live chat is one of the most effective tools for real-time customer engagement. It allows businesses to offer instant assistance right when customers need it—whether they\'re browsing your website, having trouble with a product, or deciding on a purchase.',
            'Today\'s borrowers expect immediate access to support through digital channels. Whether it\'s a quick question or a detailed inquiry, our support teams ensure your customers feel heard, valued, and supported.',
        ],
        'sections': [
            {
                'heading': 'Our live chat services provide:',
                'items': ['Real-time application support', 'Product clarification', 'Account assistance', 'Payment troubleshooting', 'Guided borrower navigation'],
                'after': 'Live chat improves conversion rates, reduces inbound call volume, and enhances borrower satisfaction.',
            },
            {
                'heading': 'Our agents are trained to:',
                'items': ['Respond quickly and clearly', 'Maintain professional tone', 'Escalate when necessary', 'Log interactions within your system'],
            },
        ],
        'closing': [
            'Digital support should enhance operational efficiency — not create fragmentation. TELEPRO ensures live chat integrates seamlessly into your servicing workflows.',
        ],
        'cta_line': "Let's enhance your customer support strategy.",
    },
    'email-support-ticket-management': {
        'title': 'Email Support & Ticket Management',
        'subtitle': 'Structured, Documented Communication',
        'image': 'images/email-support-ticket-management.png',
        'intro': [
            'Email support remains an essential communication channel for borrowers who need detailed explanations, documentation, and written confirmation of their requests or issues. Through email support, customers can clearly describe their concerns, attach necessary documents, and receive structured responses from support teams.',
            'This ensures that every borrower request is recorded, assigned to the appropriate team member, monitored for timely resolution, and maintained as a reference for future communication and service improvement.',
        ],
        'sections': [
            {
                'heading': 'Our email support services include:',
                'items': ['Structured response templates', 'Ticket categorization and prioritization', 'Escalation routing', 'SLA-aligned response times', 'Brand-consistent communication'],
            },
        ],
        'closing': [
            'Email interactions create documented records that support internal oversight and borrower clarity.',
            'We integrate directly into your ticketing systems to maintain transparency.',
        ],
        'cta_line': "Let's enhance your customer support strategy.",
    },
}


def index(request):
    return render(request, 'landingPage/index.html')


def about(request):
    return render(request, 'landingPage/about.html')


def services(request):
    return render(request, 'landingPage/services.html')


def service_detail(request, slug):
    service = SERVICES.get(slug)
    if not service:
        raise Http404('Service not found')
    return render(request, 'landingPage/service_detail.html', {
        'service': service,
        'slug': slug,
    })


def features(request):
    return render(request, 'landingPage/features.html')


def faq(request):
    return render(request, 'landingPage/faq.html')


def contact(request):
    return render(request, 'landingPage/contact.html')


def privacy(request):
    return render(request, 'landingPage/privacy.html')


def sitemap_view(request):
    return render(request, 'landingPage/sitemap.html')