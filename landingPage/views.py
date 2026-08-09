from django.shortcuts import render, get_object_or_404
from django.http import Http404


# Service data - in a real project this would be in the database
SERVICES = {
    'loan-servicing-call-center': {
        'title': 'Loan Servicing Call Center',
        'subtitle': 'Clear Communication. Reduced Friction. Stronger Borrower Confidence.',
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
    },
    'collections-call-center-for-lenders': {
        'title': 'Collections Call Center for Lenders',
        'subtitle': 'Performance-Driven. Respectful. Structured.',
        'intro': [
            'Collections communication is one of the most sensitive aspects of lending operations. Borrowers experiencing financial stress require professional, empathetic, and structured engagement.',
            'Our collections call center services are designed to improve repayment performance while maintaining borrower dignity and brand integrity.',
        ],
        'sections': [
            {
                'heading': 'We support:',
                'items': ['Early-stage delinquency outreach', 'Mid-stage recovery follow-ups', 'Promise-to-pay tracking and follow-up', 'Retention-focused repayment discussions'],
            },
            {
                'heading': 'Our structured collections framework focuses on:',
                'items': ['Clear communication of obligations', 'Documentation accuracy', 'Professional tone', 'Measurable performance metrics'],
            },
        ],
        'closing': [
            'Collections is not about pressure — it is about disciplined communication aligned with performance goals.',
        ],
    },
    'inbound-outbound-call-handling': {
        'title': 'Inbound & Outbound Call Handling',
        'subtitle': 'Professional Borrower Engagement Across Every Touchpoint',
        'intro': [
            'TELEPRO provides comprehensive inbound and outbound call handling tailored specifically to lending environments.',
            'Effective communication is at the heart of every successful customer relationship. Our services are designed to ensure that every interaction with your customers is smooth, professional, and impactful.',
        ],
        'sections': [
            {
                'heading': 'Inbound Call Handling — Key Features:',
                'items': ['Product inquiries', 'Account questions', 'Technical servicing support', 'Billing clarification', 'Complaint intake and resolution', 'General borrower support'],
            },
            {
                'heading': 'Our outbound capabilities include:',
                'items': ['Lead follow-ups', 'Application completion reminders', 'Renewal campaigns', 'Payment reminder outreach', 'Borrower satisfaction surveys', 'Re-engagement programs'],
            },
        ],
        'closing': [
            'Every call is an opportunity to strengthen your brand and deepen borrower loyalty.',
        ],
    },
    'live-chat-support': {
        'title': 'Live Chat Support',
        'subtitle': 'Real-Time Digital Engagement for Modern Borrowers',
        'intro': [
            'Live chat is one of the most effective tools for real-time customer engagement. It allows businesses to offer instant assistance right when customers need it.',
            "Today's borrowers expect immediate access to support through digital channels. Whether it's a quick question or a detailed inquiry, our support teams ensure your customers feel heard, valued, and supported.",
        ],
        'sections': [
            {
                'heading': 'Our live chat services provide:',
                'items': ['Real-time application support', 'Product clarification', 'Account assistance', 'Payment troubleshooting', 'Guided borrower navigation'],
            },
        ],
        'closing': [
            'Live chat improves conversion rates, reduces inbound call volume, and enhances borrower satisfaction.',
        ],
    },
    'email-support-ticket-management': {
        'title': 'Email Support & Ticket Management',
        'subtitle': 'Structured, Documented Communication',
        'intro': [
            'Email support remains an essential communication channel for borrowers who need detailed explanations, documentation, and written confirmation of their requests or issues.',
            'This ensures that every borrower request is recorded, assigned to the appropriate team member, monitored for timely resolution, and maintained as a reference for future communication.',
        ],
        'sections': [
            {
                'heading': 'Our email support services include:',
                'items': ['Structured response templates', 'Ticket categorization and prioritization', 'Escalation routing', 'SLA-aligned response times', 'Brand-consistent communication'],
            },
        ],
        'closing': [
            'Email support provides the documentation trail that lending operations require for compliance and accountability.',
        ],
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