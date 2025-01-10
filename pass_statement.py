import matplotlib.pyplot as plt
import matplotlib.patches as patches


def create_wbs_box(ax, x, y, width, height, text, facecolor='#ffffff', edgecolor='#666666', fontsize=10):
    # Create box with rounded corners
    box = patches.FancyBboxPatch((x, y), width, height,
                                 boxstyle="round,pad=0.02",
                                 facecolor=facecolor,
                                 edgecolor=edgecolor,
                                 linewidth=3)
    ax.add_patch(box)

    # Add text
    ax.text(x + width / 2, y + height / 2, text,
            ha='center', va='center',
            fontsize=fontsize,
            fontweight='bold',
            color='black',
            wrap=True)

    return (x + width / 2, y)


def draw_connection(ax, start, end):
    # Draw arrow connection
    ax.annotate('',
                xy=(end[0], end[1] + 0.1),
                xytext=(start[0], start[1] - 0.1),
                arrowprops=dict(arrowstyle='->',
                                connectionstyle='arc3,rad=0',
                                color='#333333',
                                linewidth=2))


# Set up the figure with higher resolution for JPEG
plt.rcParams['figure.dpi'] = 500  # Increased DPI for better JPEG quality
fig, ax = plt.subplots(figsize=(20, 12))  # Increased size for better resolution

# Box dimensions
main_width = 4
main_height = 1.2
level2_width = 3
level2_height = 0.8
level3_width = 2.5
level3_height = 0.6

# Enhanced colors for better JPEG appearance
level1_color = '#B3D9FF'  # Light blue
level2_color = '#B3E6B3'  # Light green
level3_color = '#FFD9B3'  # Light orange

# Level 1 (Main Project)
main_box = create_wbs_box(ax, 8, 8, main_width, main_height,
                          "1. TransLink Bus Fleet\nMaintenance Project",
                          facecolor=level1_color, fontsize=16)

# Level 2 (Major Phases)
phase_positions = [
    (2, 6),  # Project Initiation
    (6, 6),  # Current State
    (10, 6),  # Maintenance Strategy
    (14, 6),  # Implementation
    (18, 6),  # Monitoring
]

phase_texts = [
    "1.1 Project Initiation\nand Planning",
    "1.2 Current State\nAssessment",
    "1.3 Maintenance Strategy\nDevelopment",
    "1.4 Implementation",
    "1.5 Monitoring, Control,\nand Closure"
]

level2_boxes = []
for (x, y), text in zip(phase_positions, phase_texts):
    box = create_wbs_box(ax, x, y, level2_width, level2_height,
                         text, facecolor=level2_color, fontsize=14)
    level2_boxes.append(box)
    draw_connection(ax, main_box, box)

# Level 3 data structure
level3_data = {
    0: ["1.1.1 Develop Project Charter",
        "1.1.2 Stakeholder Identification",
        "1.1.3 Initial Project Team Assembly",
        "1.1.4 Kick-off Meeting",
        "1.1.5 Develop Project Management Plan"],
    1: ["1.2.1 Data Collection",
        "1.2.2 Gather Historical Records",
        "1.2.3 Collect Fleet Performance",
        "1.2.4 Benchmark Against Industry Standards",
        "1.2.5 Gap Analysis Report",
        "1.2.6 Estimate Production Efforts"],
    2: ["1.3.1 Define Objectives",
        "1.3.2 Develop Maintenance Protocols",
        "1.3.3 Design Scheduling System",
        "1.3.4 Develop Implementation Timeline",
        "1.3.5 Risk Assessment",
        "1.3.6 Change Management Strategy",
        "1.3.7 Training Program Development"],
    3: ["1.4.1 Pilot Implementation",
        "1.4.2 Train Maintenance Staff",
        "1.4.3 Monitor Pilot Performance",
        "1.4.4 Staff Training and Development",
        "1.4.5 Deploy Preventive Maintenance Records"],
    4: ["1.5.1 Establish Performance Metrics",
        "1.5.2 Implement Monitoring Systems",
        "1.5.3 Regular Performance Reviews",
        "1.5.4 Stakeholder Reporting",
        "1.5.5 Project Closure Report",
        "1.5.6 Celebration and Recognition"]
}

# Draw Level 3 boxes
for phase_idx, tasks in level3_data.items():
    base_x = phase_positions[phase_idx][0]
    num_tasks = len(tasks)
    total_width = num_tasks * (level3_width + 0.3)
    start_x = base_x - total_width / 2 + level3_width / 2

    for i, task in enumerate(tasks):
        x = start_x + i * (level3_width + 0.3)
        y = 4  # Lower position for level 3
        box = create_wbs_box(ax, x, y, level3_width, level3_height,
                             task, facecolor=level3_color, fontsize=12)
        draw_connection(ax, level2_boxes[phase_idx], box)

# Set the axis limits
ax.set_xlim(-1, 21)
ax.set_ylim(3, 10)
ax.set_xticks([])
ax.set_yticks([])

# Add title
plt.title('TransLink Bus Fleet Maintenance Project - Work Breakdown Structure',
          fontsize=20, pad=20, fontweight='bold')

# Remove axes
plt.axis('off')

# Adjust layout
plt.tight_layout()

# Save the figure as JPEG with high quality
plt.savefig('wbs_diagram.jpg',
            dpi=500,  # High DPI for quality
            quality=100,  # Maximum JPEG quality
            bbox_inches='tight',  # Trim excess white space
            pad_inches=0.5,  # Add some padding
            format='jpg')  # Specify JPEG format

print("WBS diagram has been saved as 'wbs_diagram.jpg'")

# Display the plot (optional)
plt.show()