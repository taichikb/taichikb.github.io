#!/usr/bin/env python3
"""Enrichment content for all 30 topics.

Each entry: list of (en_html_card, vi_html_card) tuples.
Cards get inserted before the existing master-cue section in each page.
"""


SUNG = [
    (
        "<h3>When Sōng Becomes Visible</h3>"
        "<p>Beginners often think they are relaxed because they feel soft. The teacher disagrees: they are <em>sagging</em>, not relaxing. The distinction is between a structure that is light (Sōng) and a structure that has collapsed (Sūi).</p>"
        "<p>Three visible signs of true Sōng: the shoulders sit below the ears (not lifted, not drooped); the elbows hang heavier than the hands (gravity does the work); the breath descends visibly into the lower abdomen (not held in the chest). Three visible signs of collapse: the chest caves inward, the head hangs forward, the knees lock or bend inward.</p>"
        "<p>A practical test: stand in Sōng for one minute. A neutral observer should be able to tell which posture is more &ldquo;alive&rdquo; &mdash; not by the amount of motion (both are still) but by the quality of presence. Sōng feels awake; collapse feels tired.</p>",

        "<h3>Khi Nào Tùng Trở Nên Nhìn Thấy Được</h3>"
        "<p>Người mới thường nghĩ họ thư giãn vì cảm thấy mềm. Thầy không đồng ý: họ đang <em>sụp</em>, không thư giãn. Sự phân biệt là giữa cấu trúc nhẹ (Tùng) và cấu trúc đã sụp (Tập).</p>"
        "<p>Ba dấu hiệu nhìn thấy được của Tùng thật: vai ngồi dưới tai (không nâng, không rơi); khuỷu nặng hơn bàn tay (trọng lực làm việc); hơi thở đi xuống nhìn thấy được vào bụng dưới (không giữ trong ngực). Ba dấu hiệu nhìn thấy được của sụp: ngực lõm vào trong, đầu rơi về phía trước, gối khóa hoặc gập vào trong.</p>"
        "<p>Một kiểm tra thực tế: đứng ở Tùng một phút. Một người quan sát trung lập nên có thể nói tư thế nào &ldquo;sống&rdquo; hơn &mdash; không phải bằng lượng chuyển động (cả hai đều yên) mà bằng chất lượng hiện diện. Tùng cảm thấy tỉnh; sụp cảm thấy mệt.</p>",
    ),
    (
        "<h3>Sōng Across the Body</h3>"
        "<p>Sōng is not just mental; it is <em>anatomical</em>. Nine checkpoints: crown suspended (Baihui), shoulders sunk (Jian), elbows dropped (Zhou), wrists flexible (Wan), fingers curved (Zhi), chest hollow (Xiong), waist loose (Yao), kua open (Ku), knees directional (Xi). Each is a specific anatomical instruction, not a vague instruction to &ldquo;relax.&rdquo;</p>"
        "<p>The classical phrase is <em>&ldquo;from head to foot, let everything hang&rdquo;</em>. The word &ldquo;hang&rdquo; (xuán 悬) is precise: the body is suspended from above (the crown), supported from below (the feet), with everything in between free to organise itself. A hanger relaxes; a hanger that has been pushed too tight becomes stiff. The body is the hanger; the joints are the loose folds.</p>",

        "<h3>Tùng Xuyên Suốt Cơ Thể</h3>"
        "<p>Tùng không chỉ là tinh thần; nó là <em>giải phẫu</em>. Chín điểm: đỉnh đầu treo (Bách Hội), vai chìm (Kiên), khuỷu rơi (Trửu), cổ tay mềm dẻo (Uyển), ngón tay cong (Chỉ), ngực lõm (Hưng), eo lỏng (Yêu), kua mở (Khoa), gối có hướng (Tất). Mỗi cái là một chỉ dẫn giải phẫu cụ thể, không phải chỉ dẫn mơ hồ để &ldquo;thư giãn&rdquo;.</p>"
        "<p>Câu cổ điển là <em>&ldquo;từ đầu đến chân, để mọi thứ treo&rdquo;</em>. Từ &ldquo;treo&rdquo; (huyền 悬) chính xác: cơ thể được treo từ trên (đỉnh đầu), hỗ trợ từ dưới (bàn chân), với mọi thứ ở giữa tự do tổ chức. Một cái móc thư giãn; một cái móc bị đẩy quá chặt trở nên cứng. Cơ thể là cái móc; các khớp là các nếp gấp lỏng.</p>",
    ),
]


SUNG_VS_SUI = [
    (
        "<h3>The Cost of Mixing Them Up</h3>"
        "<p>A practitioner who cannot distinguish Sōng from Sūi is doing internal damage over years. The collapsed posture (Sūi) compresses the spine, restricts the diaphragm, slows the circulation, and shortens the breath. These effects are subtle day-to-day but compound over decades into chronic fatigue, shallow breathing, and reduced mobility.</p>"
        "<p>The distinction is not academic. It is the difference between a body that is becoming more open with practice and a body that is becoming more compressed. A teacher who can tell them apart saves a student years of accumulated damage.</p>",

        "<h3>Chi Phí Khi Trộn Lẫn Hai Cái</h3>"
        "<p>Một người tập không phân biệt được Tùng và Tập đang gây hại nội tại qua nhiều năm. Tư thế sụp (Tập) nén cột sống, hạn chế cơ hoành, chậm tuần hoàn, và rút ngắn hơi thở. Những hiệu ứng này tinh tế hằng ngày nhưng cộng dồn qua nhiều thập kỷ thành mệt mỏi mãn tính, thở nông, và giảm tính di động.</p>"
        "<p>Sự phân biệt không phải lý thuyết. Đó là khác biệt giữa một cơ thể đang trở nên mở hơn với thực hành và một cơ thể đang trở nên nén hơn. Một người thầy có thể nói chúng khác nhau sẽ cứu học viên nhiều năm tổn thương tích lũy.</p>",
    ),
    (
        "<h3>What the Eye Sees in Each</h3>"
        "<p>From the side: in Sōng, the ear sits above the shoulder, which sits above the hip, which sits above the knee, which sits above the ankle. Five points on a vertical line. In Sūi, the head tilts forward of the shoulder, the shoulder rounds forward of the hip, the hip tucks under, and the knee often bends inward.</p>"
        "<p>From the front: in Sōng, the chest is hollow (a small space between chest and chin), the arms hang naturally, the kua is open. In Sūi, the chest caves (no space between chest and chin), the arms dangle without structure, the knees collapse inward.</p>"
        "<p>The teacher&rsquo;s eye learns to read these signatures in a single glance. The student&rsquo;s body learns to produce one or the other by intention. Over time, the student&rsquo;s eye sharpens too.</p>",

        "<h3>Mắt Thấy Gì Ở Mỗi Cái</h3>"
        "<p>Từ bên: trong Tùng, tai nằm trên vai, vai nằm trên hông, hông nằm trên gối, gối nằm trên cổ chân. Năm điểm trên một đường thẳng đứng. Trong Tập, đầu nghiêng về phía trước của vai, vai tròn về phía trước của hông, hông cuộn dưới, và gối thường gập vào trong.</p>"
        "<p>Từ phía trước: trong Tùng, ngực lõm (một khoảng trống nhỏ giữa ngực và cằm), tay treo tự nhiên, kua mở. Trong Tập, ngực sụp (không có khoảng trống giữa ngực và cằm), tay lủng lẳng không có cấu trúc, gối sụp vào trong.</p>"
        "<p>Mắt thầy học đọc những đặc điểm này trong một ánh nhìn. Cơ thể học viên học tạo ra cái này hoặc cái kia bằng ý chí. Theo thời gian, mắt học viên cũng sắc lại.</p>",
    ),
]


YI_DAN_KHI = [
    (
        "<h3>Yì → Qì → Jīn as a Daily Drill</h3>"
        "<p>The transmission sequence is not just a principle; it is a drill. Practise it explicitly once a day: stand in Wuji, decide (Yì) where the next movement will go, let the Qì settle into the dantian as you move, and let Jīn express itself in the hands. Three repetitions, thirty seconds each.</p>"
        "<p>The drill has two phases. In phase one, the Yì leads. You decide the movement; the body catches up. In phase two, the Yì, Qì, and Jīn fuse. You stop noticing the sequence because all three are moving together. The first phase teaches the order; the second phase teaches the integration.</p>",
        "<h3>Ý → Khí → Kình Như Bài Tập Hằng Ngày</h3>"
        "<p>Chuỗi truyền dẫn không chỉ là nguyên lý; nó là bài tập. Thực hành nó rõ ràng mỗi ngày một lần: đứng ở Vô Cực, quyết định (Ý) chuyển động tiếp theo sẽ đi đâu, để Khí an xuống Đan Điền khi bạn di chuyển, và để Kình biểu hiện ở tay. Ba lần lặp lại, mỗi lần ba mươi giây.</p>"
        "<p>Bài tập có hai pha. Trong pha một, Ý dẫn. Bạn quyết định chuyển động; cơ thể đuổi kịp. Trong pha hai, Ý, Khí, và Kình hợp nhất. Bạn ngừng nhận ra chuỗi vì cả ba đang di chuyển cùng nhau. Pha một dạy thứ tự; pha hai dạy sự tích hợp.</p>",
    ),
    (
        "<h3>When the Sequence Breaks</h3>"
        "<p>Three common ways the sequence breaks:</p>"
        "<ol>"
        "<li><strong>Body leads</strong>: you move first and try to fit Yì onto what the body is already doing. The result looks mechanical; the mind arrives late. Fix: stop, return to stillness, restart from Yì.</li>"
        "<li><strong>Breath leads</strong>: you breathe first and let the breath drag the body. The result looks floaty; the breath has no destination. Fix: give the breath a Yì-direction first; then let the body follow.</li>"
        "<li><strong>Force leads</strong>: you push first and try to organise Yì and Qì around the push. The result looks tense; the force has no internal driver. Fix: soften the force; let Yì and Qì lead; the force becomes expression, not effort.</li>"
        "</ol>"
        "<p>Each break has a different feel. The student who learns to feel which break is happening can correct it on the spot. The student who cannot will keep repeating the same broken sequence indefinitely.</p>",

        "<h3>Khi Chuỗi Bị Phá Vỡ</h3>"
        "<p>Ba cách phổ biến chuỗi bị phá vỡ:</p>"
        "<ol>"
        "<li><strong>Thân dẫn</strong>: bạn di chuyển trước và cố gắng đặt Ý lên những gì cơ thể đang làm. Kết quả trông cơ khí; tâm đến muộn. Cách sửa: dừng, trở về tĩnh lặng, khởi động lại từ Ý.</li>"
        "<li><strong>Hơi thở dẫn</strong>: bạn thở trước và để hơi thở kéo cơ thể. Kết quả trông lơ lửng; hơi thở không có đích. Cách sửa: cho hơi thở một hướng Ý trước; rồi để cơ thể theo.</li>"
        "<li><strong>Lực dẫn</strong>: bạn đẩy trước và cố gắng tổ chức Ý và Khí quanh cú đẩy. Kết quả trông căng; lực không có người lái nội tại. Cách sửa: mềm lực; để Ý và Khí dẫn; lực trở thành biểu hiện, không phải nỗ lực.</li>"
        "</ol>"
        "<p>Mỗi sự phá vỡ có một cảm giác khác nhau. Học viên học cảm nhận sự phá vỡ nào đang xảy ra có thể sửa ngay tại chỗ. Học viên không thể sẽ tiếp tục lặp lại cùng một chuỗi bị phá vỡ vô thời hạn.</p>",
    ),
]


MUSHIN = [
    (
        "<h3>Where Mushin Shows</h3>"
        "<p>Mushin is most visible in three places:</p>"
        "<ol>"
        "<li><strong>The eyes</strong>: a Mushin practitioner&rsquo;s gaze is open, soft, present. The eyes do not grip any one thing. They see what is there, not what they expect to see.</li>"
        "<li><strong>The breath</strong>: when the breath is held, the mind is gripping. When the breath is even, the mind is open. Mushin practitioners breathe even during technical work because their minds are not forcing the breath.</li>"
        "<li><strong>The hands</strong>: Mushin hands are not stiff and not floppy. They are present. They respond to whatever they touch without anticipating what they will touch.</li>"
        "</ol>"
        "<p>These three signs are reliable because they cannot be faked. A practitioner can imitate any one of them, but not all three simultaneously over time. Sustained Mushin is the real thing.</p>",

        "<h3>Vô Tâm Biểu Hiện Ở Đâu</h3>"
        "<p>Vô Tâm rõ nhất ở ba nơi:</p>"
        "<ol>"
        "<li><strong>Mắt</strong>: ánh mắt của người tập Vô Tâm mở, mềm, hiện diện. Mắt không nắm giữ bất kỳ thứ gì. Chúng thấy cái có ở đó, không phải cái họ kỳ vọng thấy.</li>"
        "<li><strong>Hơi thở</strong>: khi hơi thở bị giữ, tâm đang nắm giữ. Khi hơi thở đều, tâm đang mở. Người tập Vô Tâm thở đều trong khi làm việc kỹ thuật vì tâm họ không ép hơi thở.</li>"
        "<li><strong>Tay</strong>: tay Vô Tâm không cứng và không mềm oặt. Chúng hiện diện. Chúng đáp ứng với bất cứ gì chúng chạm mà không kỳ vọng trước.</li>"
        "</ol>"
        "<p>Ba dấu hiệu này đáng tin cậy vì chúng không thể giả. Một người tập có thể bắt chước bất kỳ một trong số chúng, nhưng không cả ba đồng thời trong thời gian dài. Vô Tâm bền bỉ là thứ thật.</p>",
    ),
    (
        "<h3>Mushin vs No-Mind in Other Traditions</h3>"
        "<p>Several Eastern traditions name a similar concept. Zen Buddhism speaks of <em>mushin</em> and <em>no-mind</em>. Daoist internal alchemy speaks of <em>wú xīn (無心)</em>. Hindu yoga speaks of <em>ahankāra-rahita</em> (without the sense of &ldquo;I am doing this&rdquo;). All four converge on the same observation: when the mind stops intervening, the action improves.</p>"
        "<p>Tai Chi&rsquo;s contribution is to operationalise this through the body. Most traditions reach no-mind through sitting meditation; Tai Chi reaches it through moving meditation. The form itself is the vehicle for emptying the mind, and the emptied mind then improves the form. This is a closed loop that strengthens with practice.</p>",

        "<h3>Vô Tâm vs Tâm-Không Trong Các Truyền Thống Khác</h3>"
        "<p>Một số truyền thống phương Đông đặt tên cho một khái niệm tương tự. Phật giáo Thiền nói về <em>mushin</em> và <em>tâm không</em>. Đạo giáo nội đan nói về <em>vô tâm (無心)</em>. Yoga Hindu nói về <em>ahankāra-rahita</em> (không có cảm giác &ldquo;tôi đang làm điều này&rdquo;). Cả bốn hội tụ ở cùng một quan sát: khi tâm ngừng can thiệp, hành động cải thiện.</p>"
        "<p>Đóng góp của Thái Cực Quyền là vận hành hóa điều này qua cơ thể. Hầu hết các truyền thống đạt đến tâm không qua thiền ngồi; Thái Cực Quyền đạt đến nó qua thiền động. Bài quyền chính là phương tiện làm trống tâm, và tâm đã trống thì cải thiện bài quyền. Đây là một vòng lặp kín củng cố qua thực hành.</p>",
    ),
]


OM_THU = [
    (
        "<h3>What Standing Meditation Does</h3>"
        "<p>Zhan Zhuang (Trụ Thế) does three things at once. <strong>Biomechanically</strong>, it teaches the body to stand with the integrated skeleton, the dropped shoulders, the open kua, the grounded feet. <strong>Neurologically</strong>, it teaches the nervous system to hold a posture without gripping. <strong>Energetically</strong>, it teaches the breath to descend and the dantian to fill.</p>"
        "<p>Most students experience the benefits in this order: first biomechanical (the body learns to stand), then neurological (the mind learns to be still in the body), then energetic (the breath learns to descend). Each stage takes longer than the one before. The biomechanical benefits appear in weeks; the neurological in months; the energetic in years.</p>",

        "<h3>Thiền Đứng Làm Gì</h3>"
        "<p>Trụ Thế làm ba thứ cùng một lúc. <strong>Về cơ sinh học</strong>, nó dạy cơ thể đứng với bộ xương tích hợp, vai hạ, kua mở, chân neo. <strong>Về thần kinh</strong>, nó dạy hệ thần kinh giữ tư thế mà không nắm giữ. <strong>Về năng lượng</strong>, nó dạy hơi thở đi xuống và Đan Điền đầy.</p>"
        "<p>Hầu hết học viên trải nghiệm lợi ích theo thứ tự này: trước tiên cơ sinh học (cơ thể học đứng), sau đó thần kinh (tâm học yên trong cơ thể), sau đó năng lượng (hơi thở học đi xuống). Mỗi giai đoạn mất nhiều thời gian hơn giai đoạn trước. Lợi ích cơ sinh học xuất hiện trong vài tuần; thần kinh trong vài tháng; năng lượng trong vài năm.</p>",
    ),
    (
        "<h3>Common Distortions and Their Meanings</h3>"
        "<p>After three to five minutes of standing, the body reports. The reports arrive as physical sensations that are not random &mdash; they are messages from the body about its current organisation:</p>"
        "<ul>"
        "<li><strong>Shoulder ache</strong>: the trapezius is holding tension that the body does not need. Release it by dropping the elbows and letting the shoulders fall.</li>"
        "<li><strong>Lower back ache</strong>: the lumbar spine is not suspended; the lower back is doing structural work that the dantian and the legs should do. Sink the tailbone slightly and let the spine lengthen.</li>"
        "<li><strong>Knee discomfort</strong>: the kua is closed; the knee is being asked to absorb forces the hip should absorb. Open the kua by releasing the inner thighs and the hip rotators.</li>"
        "<li><strong>Calf trembling</strong>: the calf is doing too much work; the weight is on the heels instead of the soles. Shift the weight slightly forward into the bubbling-well point.</li>"
        "<li><strong>Foot numbness</strong>: circulation is restricted; the body is gripping the floor. Release the toes; let the foot spread naturally on the ground.</li>"
        "</ul>"
        "<p>Each report is a diagnostic. The student who listens to the reports and corrects them in real time is doing <em>internal medicine</em> through posture.</p>",

        "<h3>Các Méo Mó Phổ Biến Và Ý Nghĩa</h3>"
        "<p>Sau ba đến năm phút đứng, cơ thể báo cáo. Các báo cáo đến dưới dạng cảm giác vật lý không ngẫu nhiên &mdash; chúng là thông điệp từ cơ thể về tổ chức hiện tại:</p>"
        "<ul>"
        "<li><strong>Đau vai</strong>: cơ thang đang giữ căng thẳng mà cơ thể không cần. Thả nó bằng cách hạ khuỷu và để vai rơi.</li>"
        "<li><strong>Đau lưng dưới</strong>: cột sống thắt lưng không được treo; lưng dưới đang làm việc cấu trúc mà Đan Điền và chân nên làm. Hạ xương cụt nhẹ và để cột sống dài ra.</li>"
        "<li><strong>Khó chịu gối</strong>: kua đóng; gối đang được yêu cầu hấp thụ lực mà hông nên hấp thụ. Mở kua bằng cách thả mặt trong đùi và các cơ xoay hông.</li>"
        "<li><strong>Bắp chân run</strong>: bắp chân đang làm quá nhiều việc; trọng lượng ở gót thay vì lòng bàn chân. Chuyển trọng lượng hơi về phía trước vào huyệt Dũng Tuyền.</li>"
        "<li><strong>Tê chân</strong>: tuần hoàn bị hạn chế; cơ thể đang nắm sàn. Thả ngón chân; để chân lan tự nhiên trên đất.</li>"
        "</ul>"
        "<p>Mỗi báo cáo là chẩn đoán. Học viên lắng nghe các báo cáo và sửa chúng theo thời gian thực đang làm <em>y học nội tại</em> qua tư thế.</p>",
    ),
]


CHAM_LA_NHANH = [
    (
        "<h3>How Slow Practice Builds Speed</h3>"
        "<p>Slow practice builds speed through three mechanisms:</p>"
        "<ol>"
        "<li><strong>Neural pathway refinement</strong>: each slow repetition lays down a clearer motor pathway in the cerebellum and basal ganglia. When the movement is later performed at speed, the brain has a clearer template to follow.</li>"
        "<li><strong>Muscle spindle calibration</strong>: slow movement allows the muscle spindles (which sense length and rate of change) to be calibrated against the actual requirements of the movement. Fast movement does not allow this calibration; the spindles are guessing.</li>"
        "<li><strong>Breath coordination</strong>: slow movement allows the breath to find the movement; fast movement forces the breath to scramble to keep up.</li>"
        "</ol>"
        "<p>None of these mechanisms operates during fast practice. Speed without slow is speed without foundation.</p>",

        "<h3>Thực Hành Chậm Xây Dựng Tốc Độ Như Thế Nào</h3>"
        "<p>Thực hành chậm xây dựng tốc độ qua ba cơ chế:</p>"
        "<ol>"
        "<li><strong>Tinh chỉnh đường thần kinh</strong>: mỗi lần lặp chậm tạo ra một đường vận động rõ hơn trong tiểu não và hạch nền. Khi chuyển động sau đó được thực hiện ở tốc độ, não có một khuôn mẫu rõ hơn để theo.</li>"
        "<li><strong>Hiệu chỉnh thoi cơ</strong>: chuyển động chậm cho phép thoi cơ (cảm nhận chiều dài và tốc độ thay đổi) được hiệu chỉnh theo yêu cầu thực tế của chuyển động. Chuyển động nhanh không cho phép hiệu chỉnh này; thoi cơ đang đoán.</li>"
        "<li><strong>Phối hợp hơi thở</strong>: chuyển động chậm cho phép hơi thở tìm chuyển động; chuyển động nhanh ép hơi thở phải vội vã để theo kịp.</li>"
        "</ol>"
        "<p>Không cơ chế nào trong số này hoạt động trong thực hành nhanh. Tốc độ không có chậm là tốc độ không có nền tảng.</p>",
    ),
    (
        "<h3>The 30% Test</h3>"
        "<p>A simple diagnostic: do the form at 30% of normal speed for three minutes. If the form remains structurally intact (waist loose, kua open, feet grounded, breath descending), you have the foundation. If the form collapses at 30% (joints lock, breath rises, weight floats), the foundation is missing and speed will only expose it.</p>"
        "<p>Many students discover at 30% that they were using speed to hide tension. The shoulders were held because the form moved through them quickly. The breath was short because the form demanded fast transitions. At 30%, the hiding place is gone. What was hidden is now visible.</p>",

        "<h3>Kiểm Tra 30%</h3>"
        "<p>Một chẩn đoán đơn giản: thực hiện bài quyền ở 30% tốc độ bình thường trong ba phút. Nếu bài quyền vẫn còn nguyên vẹn cấu trúc (eo lỏng, kua mở, chân neo, hơi thở đi xuống), bạn có nền tảng. Nếu bài quyền sụp ở 30% (khớp khóa, hơi thở dâng, trọng lượng nổi), nền tảng thiếu và tốc độ sẽ chỉ phơi bày nó.</p>"
        "<p>Nhiều học viên phát hiện ở 30% rằng họ đang dùng tốc độ để giấu căng thẳng. Vai được giữ vì bài quyền đi qua chúng nhanh. Hơi thở ngắn vì bài quyền đòi hỏi chuyển tiếp nhanh. Ở 30%, nơi giấu đã đi. Cái bị giấu giờ nhìn thấy được.</p>",
    ),
]


TAN_HU_TAN_THUC = [
    (
        "<h3>The Three-Step Rhythm</h3>"
        "<p>Every step in the form has three phases: <strong>transfer</strong> (weight moves toward the target foot), <strong>place</strong> (the foot contacts the ground, still empty), <strong>settle</strong> (the foot becomes full and the back foot lifts). The error is to skip the place phase &mdash; to plant the foot and only then transfer weight. This collapses the wave into a stamp.</p>"
        "<p>The rhythm is a wave, not a stamp. A wave has a rising phase (transfer), a peak (place), and a falling phase (settle). A stamp has only a contact and a lift. The wave teaches the body to negotiate transitions; the stamp teaches the body to interrupt them. Tai Chi wants the wave.</p>",

        "<h3>Nhịp Ba Bước</h3>"
        "<p>Mỗi bước trong bài quyền có ba pha: <strong>chuyển</strong> (trọng lượng di chuyển về phía chân đích), <strong>đặt</strong> (chân tiếp xúc đất, vẫn hư), <strong>an</strong> (chân trở thành thực và chân sau nâng). Lỗi là bỏ qua pha đặt &mdash; trồng chân rồi mới chuyển trọng lượng. Điều này làm sóng sụp thành dấu.</p>"
        "<p>Nhịp là sóng, không phải dấu. Sóng có pha dâng (chuyển), đỉnh (đặt), và pha hạ (an). Dấu chỉ có tiếp xúc và nâng. Sóng dạy cơ thể thương lượng các chuyển tiếp; dấu dạy cơ thể ngắt chúng. Thái Cực Quyền muốn sóng.</p>",
    ),
    (
        "<h3>Empty Step vs Empty Mind</h3>"
        "<p>An empty step is a deliberate lightness. The back foot leaves the ground only when it has <em>nothing more to do</em>. This is a different thing from a distracted step where the back foot lifts because the mind has wandered to the next movement.</p>"
        "<p>The difference is observable: in a deliberate empty step, the back foot lifts smoothly, the body weight is clearly on the front foot, and the breathing is even. In a distracted empty step, the back foot drags or lifts abruptly, the body weight is unclear, and the breathing is shallow or held. The first is empty in the Tai Chi sense; the second is empty in the absent sense.</p>",

        "<h3>Bước Hư vs Tâm Hư</h3>"
        "<p>Bước hư là sự nhẹ nhàng có chủ đích. Chân sau rời mặt đất chỉ khi nó <em>không còn gì để làm</em>. Đây là điều khác với bước mất tập trung nơi chân sau nâng vì tâm đã lang thang đến chuyển động tiếp theo.</p>"
        "<p>Sự khác biệt có thể quan sát được: trong bước hư có chủ đích, chân sau nâng mượt mà, trọng lượng cơ thể rõ ràng ở chân trước, và hơi thở đều. Trong bước hư mất tập trung, chân sau kéo lê hoặc nâng đột ngột, trọng lượng cơ thể không rõ, và hơi thở nông hoặc bị giữ. Cái thứ nhất là hư theo nghĩa Thái Cực; cái thứ hai là hư theo nghĩa vắng mặt.</p>",
    ),
]


NGHICH_THO = [
    (
        "<h3>Why the Reversal Works</h3>"
        "<p>Normal breathing creates positive pressure in the abdomen on exhale (the breath pushes out). Reverse breathing creates negative pressure in the abdomen on inhale (the breath pulls in). The reversal generates an internal pump effect: the lower abdomen fills on exhale, empties on inhale, in opposition to the chest.</p>"
        "<p>This pump effect massages the internal organs, increases venous return to the heart (improving circulation), and creates a downward pressure gradient that supports the lower dantian. Over months of daily practice, the pump strengthens the connection between breath and dantian &mdash; a connection that is weaker in normal breathing.</p>",

        "<h3>Tại Sao Sự Đảo Ngược Hoạt Động</h3>"
        "<p>Thở bình thường tạo áp suất dương trong bụng khi thở ra (hơi thở đẩy ra). Thở ngược tạo áp suất âm trong bụng khi hít vào (hơi thở hút vào). Sự đảo ngược tạo hiệu ứng bơm nội tại: bụng dưới đầy khi thở ra, trống khi hít vào, đối lập với ngực.</p>"
        "<p>Hiệu ứng bơm này xoa bóp các cơ quan nội tạng, tăng máu tĩnh mạch trở về tim (cải thiện tuần hoàn), và tạo gradient áp suất đi xuống hỗ trợ Đan Điền dưới. Qua nhiều tháng thực hành hằng ngày, bơm củng cố kết nối giữa hơi thở và Đan Điền &mdash; một kết nối yếu hơn trong thở bình thường.</p>",
    ),
    (
        "<h3>How to Know You're Ready</h3>"
        "<p>Three signs that you are ready to try reverse breathing:</p>"
        "<ol>"
        "<li><strong>Lower dantian breathing is automatic</strong>: you no longer need to remind yourself to breathe into the lower abdomen. It happens without intention.</li>"
        "<li><strong>Your breath rate has slowed naturally</strong>: from a typical 15&ndash;18 breaths/minute, you have dropped to 8&ndash;12 breaths/minute during practice. This is the body's preparation for deeper breath work.</li>"
        "<li><strong>You can hold a quiet standing posture for 10&ndash;15 minutes</strong>: the body has enough stillness and structural integrity to manage the more demanding mechanics of reverse breathing.</li>"
        "</ol>"
        "<p>If any of these signs are missing, continue normal dantian breathing for another season. Reverse breathing is a tool for the prepared body, not a shortcut to the prepared body.</p>",

        "<h3>Cách Biết Bạn Đã Sẵn Sàng</h3>"
        "<p>Ba dấu hiệu bạn đã sẵn sàng thử thở ngược:</p>"
        "<ol>"
        "<li><strong>Thở Đan Điền dưới đã tự động</strong>: bạn không còn cần nhắc mình thở vào bụng dưới. Nó xảy ra không cần ý chí.</li>"
        "<li><strong>Tốc độ hơi thở đã chậm tự nhiên</strong>: từ 15&ndash;18 nhịp/phút điển hình, bạn đã giảm xuống 8&ndash;12 nhịp/phút trong thực hành. Đây là sự chuẩn bị của cơ thể cho công việc hơi thở sâu hơn.</li>"
        "<li><strong>Bạn có thể giữ tư thế đứng yên trong 10&ndash;15 phút</strong>: cơ thể đã có đủ tĩnh lặng và toàn vẹn cấu trúc để quản lý cơ chế đòi hỏi hơn của thở ngược.</li>"
        "</ol>"
        "<p>Nếu bất kỳ dấu hiệu nào thiếu, tiếp tục thở Đan Điền bình thường thêm một mùa. Thở ngược là công cụ cho cơ thể đã chuẩn bị, không phải lối tắt đến cơ thể đã chuẩn bị.</p>",
    ),
]


NAM_PHUT_TRU_THE = [
    (
        "<h3>What Five Minutes Does That One Minute Doesn't</h3>"
        "<p>One minute of Zhan Zhuang is barely enough time for the body to settle. Five minutes allows the body to settle, the mind to wander and return, the breath to descend, and the posture to begin to reveal its flaws. Each of these is necessary; none of them happens in one minute.</p>"
        "<p>The five-minute standard is widely cited in Tai Chi schools for a reason. Below five minutes, the practice is too short to be transformative. Above thirty minutes, it becomes demanding for most beginners. Five to fifteen minutes is the band where the practice actually works on the body.</p>",

        "<h3>Năm Phút Làm Gì Mà Một Phút Không</h3>"
        "<p>Một phút Trụ Thế vừa đủ để cơ thể an trụ. Năm phút cho phép cơ thể an trụ, tâm lang thang và trở lại, hơi thở đi xuống, và tư thế bắt đầu tiết lộ khuyết điểm của nó. Mỗi điều này cần thiết; không điều nào xảy ra trong một phút.</p>"
        "<p>Tiêu chuẩn năm phút được trích dẫn rộng rãi trong các trường phái Thái Cực Quyền vì một lý do. Dưới năm phút, thực hành quá ngắn để biến đổi. Trên ba mươi phút, nó trở nên đòi hỏi đối với hầu hết người mới. Năm đến mười lăm phút là khoảng nơi thực hành thực sự tác động lên cơ thể.</p>",
    ),
    (
        "<h3>The 30-Day Effect</h3>"
        "<p>What changes over thirty days of daily five-minute Zhan Zhuang:</p>"
        "<ul>"
        "<li><strong>Day 1&ndash;7</strong>: shoulders release; breathing visibly descends; lower back softens.</li>"
        "<li><strong>Day 8&ndash;14</strong>: standing posture improves spontaneously (not just during practice); walking feels lighter.</li>"
        "<li><strong>Day 15&ndash;21</strong>: the slow form begins to feel easier; the breath leads the movement naturally.</li>"
        "<li><strong>Day 22&ndash;30</strong>: the practice has a hold on the body that does not require willpower. Missing a day feels uncomfortable.</li>"
        "</ul>"
        "<p>This is the minimum dose. More is better. But thirty days of daily five minutes is what creates the foundation for everything that follows.</p>",

        "<h3>Hiệu Ứng 30 Ngày</h3>"
        "<p>Điều gì thay đổi qua ba mươi ngày năm phút Trụ Thế hằng ngày:</p>"
        "<ul>"
        "<li><strong>Ngày 1&ndash;7</strong>: vai thả; hơi thở đi xuống nhìn thấy được; lưng dưới mềm.</li>"
        "<li><strong>Ngày 8&ndash;14</strong>: tư thế đứng cải thiện tự phát (không chỉ trong thực hành); bước đi cảm thấy nhẹ hơn.</li>"
        "<li><strong>Ngày 15&ndash;21</strong>: bài quyền chậm bắt đầu cảm thấy dễ hơn; hơi thở dẫn chuyển động tự nhiên.</li>"
        "<li><strong>Ngày 22&ndash;30</strong>: thực hành có một giữ chặt trên cơ thể không cần ý chí. Bỏ một ngày cảm thấy khó chịu.</li>"
        "</ul>"
        "<p>Đây là liều tối thiểu. Nhiều hơn thì tốt hơn. Nhưng ba mươi ngày năm phút mỗi ngày là thứ tạo nền tảng cho mọi thứ theo sau.</p>",
    ),
]


BAI_30_PHUT = [
    (
        "<h3>What Belongs in Each Third</h3>"
        "<p>The three blocks serve three purposes:</p>"
        "<ol>"
        "<li><strong>Warm-up (body)</strong>: this is preparation, not practice. It teaches the body to arrive at the form already organised. Anything done here reduces the form&rsquo;s workload. Common warm-ups: ankle rotations, hip circles, shoulder rolls, gentle spinal twists, ten slow breaths.</li>"
        "<li><strong>Form (form)</strong>: this is the practice. One or two full repetitions of the current form, at a speed where the body can hold the structure. Do not try to do more; do less with more attention.</li>"
        "<li><strong>Cool-down (heart)</strong>: this is integration. Self-massage along the meridians, three slow breaths, a moment of stillness. The cool-down teaches the body to carry the practice into the rest of the day.</li>"
        "</ol>",
        "<h3>Mỗi Phần Ba Có Gì</h3>"
        "<p>Ba khối phục vụ ba mục đích:</p>"
        "<ol>"
        "<li><strong>Khởi động (thân)</strong>: đây là chuẩn bị, không phải thực hành. Nó dạy cơ thể đến bài quyền đã tổ chức. Bất cứ gì làm ở đây giảm khối lượng công việc của bài quyền. Khởi động phổ biến: xoay cổ chân, xoay hông, xoay vai, xoay cột sống nhẹ, mười hơi thở chậm.</li>"
        "<li><strong>Bài quyền (bài)</strong>: đây là thực hành. Một hoặc hai lần bài quyền hiện tại đầy đủ, ở tốc độ mà cơ thể có thể giữ cấu trúc. Đừng cố làm nhiều hơn; làm ít với nhiều chú ý hơn.</li>"
        "<li><strong>Hạ nhiệt (tâm)</strong>: đây là tích hợp. Tự xoa bóp dọc kinh mạch, ba hơi thở chậm, một khoảnh khắc tĩnh lặng. Hạ nhiệt dạy cơ thể mang thực hành vào phần còn lại của ngày.</li>"
        "</ol>",
    ),
    (
        "<h3>When to Shorten, When to Lengthen</h3>"
        "<p>The thirty-minute structure is a default, not a law. Some days call for shorter; some days call for longer.</p>"
        "<ul>"
        "<li><strong>Shorten to 15 minutes</strong>: when the body is tired, the schedule is tight, or the mind is agitated. Five minutes warm-up, eight minutes form, two minutes cool-down. Something is always better than nothing.</li>"
        "<li><strong>Lengthen to 60 minutes</strong>: on weekends or rest days, when the body is rested and the schedule allows. Add a fourth block: silent sitting meditation (10 minutes) between the form and the cool-down. This is where the practice deepens.</li>"
        "</ul>"
        "<p>The discipline is not the thirty-minute structure. The discipline is showing up daily. The structure is the container; showing up is the content.</p>",

        "<h3>Khi Nào Rút Ngắn, Khi Nào Kéo Dài</h3>"
        "<p>Cấu trúc ba mươi phút là mặc định, không phải luật. Một số ngày gọi ngắn hơn; một số ngày gọi dài hơn.</p>"
        "<ul>"
        "<li><strong>Rút ngắn xuống 15 phút</strong>: khi cơ thể mệt, lịch trình chật, hoặc tâm kích động. Năm phút khởi động, tám phút bài quyền, hai phút hạ nhiệt. Cái gì đó luôn tốt hơn không có gì.</li>"
        "<li><strong>Kéo dài đến 60 phút</strong>: vào cuối tuần hoặc ngày nghỉ, khi cơ thể nghỉ ngơi và lịch trình cho phép. Thêm khối thứ tư: thiền ngồi yên lặng (10 phút) giữa bài quyền và hạ nhiệt. Đây là nơi thực hành sâu hơn.</li>"
        "</ul>"
        "<p>Kỷ luật không phải cấu trúc ba mươi phút. Kỷ luật là xuất hiện hằng ngày. Cấu trúc là vỏ chứa; xuất hiện là nội dung.</p>",
    ),
]


CO_THE_SAU_50 = [
    (
        "<h3>What Does Not Change With Age</h3>"
        "<p>Five things the 50+ body keeps, even as it loses other capacities:</p>"
        "<ol>"
        "<li><strong>Proprioceptive wisdom</strong>: decades of movement have built a rich internal map of where the body is in space. Tai Chi taps this map.</li>"
        "<li><strong>Pattern recognition</strong>: the brain that has spent fifty years learning still learns. Tai Chi gives it something worth learning.</li>"
        "<li><strong>Emotional regulation</strong>: the 50+ nervous system is more experienced at returning to baseline. Tai Chi gives it a daily return.</li>"
        "<li><strong>Community capacity</strong>: the 50+ adult typically has more stable social ties than at any earlier age. Tai Chi gives it a community to join.</li>"
        "<li><strong>Wisdom of restraint</strong>: the 50+ body has learned what not to do. Tai Chi turns this restraint into a positive practice.</li>"
        "</ol>",
        "<h3>Điều Không Thay Đổi Theo Tuổi Tác</h3>"
        "<p>Năm điều cơ thể 50+ giữ được, ngay cả khi mất các năng lực khác:</p>"
        "<ol>"
        "<li><strong>Trí tuệ cảm giác bản thể</strong>: hàng thập kỷ chuyển động đã xây dựng một bản đồ nội tại phong phú về vị trí cơ thể trong không gian. Thái Cực Quyền khai thác bản đồ này.</li>"
        "<li><strong>Nhận dạng mẫu</strong>: bộ não đã học năm mươi năm vẫn học. Thái Cực Quyền cho nó thứ đáng học.</li>"
        "<li><strong>Điều hòa cảm xúc</strong>: hệ thần kinh 50+ có nhiều kinh nghiệm hơn về việc trở về đường cơ sở. Thái Cực Quyền cho nó sự trở về hằng ngày.</li>"
        "<li><strong>Năng lực cộng đồng</strong>: người lớn 50+ điển hình có các mối quan hệ xã hội ổn định hơn ở bất kỳ tuổi nào trước đó. Thái Cực Quyền cho nó một cộng đồng để tham gia.</li>"
        "<li><strong>Trí tuệ hạn chế</strong>: cơ thể 50+ đã học những gì không nên làm. Thái Cực Quyền biến sự hạn chế này thành thực hành tích cực.</li>"
        "</ol>",
    ),
    (
        "<h3>The Three-Year Promise</h3>"
        "<p>If you start Tai Chi at 52 and practise daily for three years, expect three things to be measurably different at 55:</p>"
        "<ol>"
        "<li><strong>Falls per year</strong>: down by 50&ndash;70%. The balance training, proprioceptive refinement, and bone-density maintenance compound into a measurable fall reduction.</li>"
        "<li><strong>Systolic blood pressure</strong>: down by 10&ndash;20 mmHg. The breath work, parasympathetic activation, and reduced cortisol all contribute.</li>"
        "<li><strong>Sleep quality</strong>: up by one full sleep cycle per night. The vagal tone improvement, evening routine structure, and reduced sympathetic activation at bedtime all contribute.</li>"
        "</ol>"
        "<p>None of these are guaranteed. They are statistically expected outcomes from a daily practice. The three-year horizon is the time at which the outcomes become measurable by anyone &mdash; including your doctor.</p>",

        "<h3>Lời Hứa Ba Năm</h3>"
        "<p>Nếu bạn bắt đầu Thái Cực Quyền ở tuổi 52 và tập hằng ngày trong ba năm, hãy kỳ vọng ba điều sẽ khác biệt có thể đo lường được ở tuổi 55:</p>"
        "<ol>"
        "<li><strong>Số lần té mỗi năm</strong>: giảm 50&ndash;70%. Tập thăng bằng, tinh chỉnh cảm giác bản thể, và duy trì mật độ xương cộng dồn thành giảm té có thể đo được.</li>"
        "<li><strong>Huyết áp tâm thu</strong>: giảm 10&ndash;20 mmHg. Công việc hơi thở, kích hoạt hệ phó giao cảm, và giảm cortisol đều đóng góp.</li>"
        "<li><strong>Chất lượng giấc ngủ</strong>: tăng một chu kỳ giấc ngủ đầy đủ mỗi đêm. Cải thiện trương lực phế vị, cấu trúc thói quen buổi tối, và giảm kích hoạt hệ giao cảm khi đi ngủ đều đóng góp.</li>"
        "</ol>"
        "<p>Không điều nào trong số này được đảm bảo. Chúng là kết quả thống kê được kỳ vọng từ thực hành hằng ngày. Tầm nhìn ba năm là thời điểm kết quả trở nên có thể đo lường được bởi bất kỳ ai &mdash; bao gồm bác sĩ của bạn.</p>",
    ),
]


BA_DIEU_KIEN_CHUA_LANH = [
    (
        "<h3>How the Evidence Was Gathered</h3>"
        "<p>Most of the studies behind these three healing targets are <strong>randomized controlled trials</strong> (RCTs) &mdash; the gold standard for medical evidence. RCTs work by randomly assigning participants to either a Tai Chi group or a control group, then measuring outcomes over weeks or months. The randomization removes selection bias; the controls give a baseline.</p>"
        "<p>The fall-prevention evidence, for instance, comes from the 2020 JAMA Internal Medicine meta-analysis: 32 RCTs, more than 4,000 participants, all older adults. The blood-pressure evidence comes from the 2017 JAHA meta-analysis: 69 RCTs, more than 6,000 participants. The sleep evidence comes from multiple smaller trials and one 25-week Emory study. In all three cases, the effect size was not marginal &mdash; it was large enough to be meaningful for the individual patient.</p>",

        "<h3>Bằng Chứng Được Thu Thập Như Thế Nào</h3>"
        "<p>Hầu hết các nghiên cứu đằng sau ba mục tiêu chữa lành này là <strong>thử nghiệm ngẫu nhiên có đối chứng</strong> (RCT) &mdash; tiêu chuẩn vàng cho bằng chứng y khoa. RCT hoạt động bằng cách phân ngẫu nhiên người tham gia vào nhóm Thái Cực Quyền hoặc nhóm đối chứng, sau đó đo lường kết quả qua nhiều tuần hoặc tháng. Việc phân ngẫu nhiên loại bỏ thiên kiến chọn lọc; các nhóm đối chứng cho đường cơ sở.</p>"
        "<p>Bằng chứng phòng ngừa té, ví dụ, đến từ phân tích tổng hợp JAMA Internal Medicine 2020: 32 RCT, hơn 4.000 người tham gia, tất cả người lớn tuổi. Bằng chứng huyết áp đến từ phân tích JAHA 2017: 69 RCT, hơn 6.000 người tham gia. Bằng chứng giấc ngủ đến từ nhiều thử nghiệm nhỏ hơn và một nghiên cứu Emory 25 tuần. Trong cả ba trường hợp, kích thước hiệu ứng không nhỏ &mdash; nó đủ lớn để có ý nghĩa cho bệnh nhân cá nhân.</p>",
    ),
    (
        "<h3>Why These Three and Not Others</h3>"
        "<p>Tai Chi probably improves more than three conditions &mdash; the evidence is growing for osteoarthritis, chronic pain, dementia risk, and depression. But the evidence is currently strongest for balance, blood pressure, and sleep. These three have the most RCTs, the largest meta-analyses, and the most consistent effect sizes.</p>"
        "<p>Why these three specifically? Because they all involve the autonomic nervous system (ANS). The ANS regulates balance (through vestibular reflexes and muscle tone), blood pressure (through vascular tone and heart rate), and sleep (through circadian rhythm and arousal). Tai Chi&rsquo;s breath work, slow movement, and mindfulness all operate on the ANS. The mechanism is shared; the outcomes are three.</p>",

        "<h3>Tại Sao Ba Cái Này Mà Không Phải Cái Khác</h3>"
        "<p>Thái Cực Quyền có lẽ cải thiện nhiều hơn ba điều kiện &mdash; bằng chứng đang tăng cho thoái hóa khớp, đau mãn tính, nguy cơ sa sút trí tuệ, và trầm cảm. Nhưng bằng chứng hiện mạnh nhất cho thăng bằng, huyết áp, và giấc ngủ. Ba cái này có nhiều RCT nhất, các phân tích tổng hợp lớn nhất, và kích thước hiệu ứng nhất quán nhất.</p>"
        "<p>Tại sao ba cái này cụ thể? Bởi vì chúng đều liên quan đến hệ thần kinh tự trị (ANS). ANS điều hòa thăng bằng (qua phản xạ tiền đình và trương lực cơ), huyết áp (qua trương lực mạch máu và nhịp tim), và giấc ngủ (qua nhịp sinh học và hưng phấn). Công việc hơi thở, chuyển động chậm, và chánh niệm của Thái Cực Quyền đều tác động lên ANS. Cơ chế chia sẻ; kết quả là ba.</p>",
    ),
]


TAP_20_PHUT_TAI_NHA = [
    (
        "<h3>What to Do When You're Travelling</h3>"
        "<p>Travel disrupts every routine. The 20-minute home practice survives travel better than longer practices because it requires no equipment, no specific space, and no specific clothing.</p>"
        "<p>Three adaptations for travel:</p>"
        "<ol>"
        "<li><strong>Hotel room</strong>: stand rather than lie for the Zhan Zhuang block. Use the bed or a chair for the form. The 20 minutes will be tighter than at home; that is fine.</li>"
        "<li><strong>Airplane</strong>: do the breath-only version. Five minutes dantian breathing, five minutes seated Zhan Zhuang (arms in front as if holding a ball), five minutes slow arm rotations, five minutes dantian breathing. No standing required.</li>"
        "<li><strong>Outdoors</strong>: use the new environment as the warm-up. Stand on unfamiliar ground; let the body adjust to the new proprioceptive input. This is itself a form of practice.</li>"
        "</ol>",
        "<h3>Khi Đi Du Lịch</h3>"
        "<p>Du lịch phá vỡ mọi thói quen. Thực hành 20 phút tại nhà sống sót qua du lịch tốt hơn các thực hành dài hơn vì không yêu cầu thiết bị, không gian cụ thể, và quần áo cụ thể.</p>"
        "<p>Ba thích ứng cho du lịch:</p>"
        "<ol>"
        "<li><strong>Phòng khách sạn</strong>: đứng thay vì nằm cho khối Trụ Thế. Dùng giường hoặc ghế cho bài quyền. 20 phút sẽ chật hơn ở nhà; điều đó ổn.</li>"
        "<li><strong>Máy bay</strong>: làm phiên bản chỉ thở. Năm phút thở Đan Điền, năm phút Trụ Thế ngồi (tay trước mặt như cầm bóng), năm phút xoay tay chậm, năm phút thở Đan Điền. Không yêu cầu đứng.</li>"
        "<li><strong>Ngoài trời</strong>: dùng môi trường mới làm khởi động. Đứng trên đất lạ; để cơ thể điều chỉnh với đầu vào cảm giác bản thể mới. Đây tự nó là một hình thức thực hành.</li>"
        "</ol>",
    ),
    (
        "<h3>The 20-Minute Practice Over Months</h3>"
        "<p>What changes in the 20-minute practice over six months of daily use:</p>"
        "<ul>"
        "<li><strong>Month 1</strong>: the practice feels long. The body settles into the Zhan Zhuang only in the last minute. The form feels mechanical.</li>"
        "<li><strong>Month 2</strong>: the practice feels familiar. The body settles into the Zhan Zhuang within 2 minutes. The form begins to feel less mechanical.</li>"
        "<li><strong>Month 3</strong>: the practice begins to feel short. The body settles immediately. The form begins to feel like a conversation rather than a recitation.</li>"
        "<li><strong>Month 6</strong>: the 20 minutes is not enough. The body wants more. The form has developed internal variety: the same movements feel different each day.</li>"
        "</ul>",
        "<h3>Thực Hành 20 Phút Qua Nhiều Tháng</h3>"
        "<p>Điều gì thay đổi trong thực hành 20 phút qua sáu tháng sử dụng hằng ngày:</p>"
        "<ul>"
        "<li><strong>Tháng 1</strong>: thực hành cảm thấy dài. Cơ thể an trụ vào Trụ Thế chỉ trong phút cuối. Bài quyền cảm thấy cơ khí.</li>"
        "<li><strong>Tháng 2</strong>: thực hành cảm thấy quen thuộc. Cơ thể an trụ vào Trụ Thế trong 2 phút. Bài quyền bắt đầu cảm thấy bớt cơ khí.</li>"
        "<li><strong>Tháng 3</strong>: thực hành bắt đầu cảm thấy ngắn. Cơ thể an trụ ngay lập tức. Bài quyền bắt đầu cảm thấy như cuộc đối thoại thay vì đọc thuộc lòng.</li>"
        "<li><strong>Tháng 6</strong>: 20 phút không đủ. Cơ thể muốn nhiều hơn. Bài quyền đã phát triển sự đa dạng nội tại: cùng chuyển động cảm thấy khác nhau mỗi ngày.</li>"
        "</ul>",
    ),
]


RESET_5_PHUT = [
    (
        "<h3>When to Use the Reset</h3>"
        "<p>The Reset is not a substitute for practice. It is a bridge between practices &mdash; what you do when the practice is not available.</p>"
        "<p>Five situations where the Reset earns its name:</p>"
        "<ol>"
        "<li><strong>Mid-day energy crash</strong>: 2pm slump. The Reset (especially the dantian breathing) restores parasympathetic tone and lifts the energy without caffeine.</li>"
        "<li><strong>Pre-meeting calm</strong>: a hard meeting is in ten minutes. The Reset settles the breath and the mind so the meeting starts from a calmer baseline.</li>"
        "<li><strong>Post-meeting recovery</strong>: a hard meeting just ended. The Reset discharges the sympathetic arousal that the meeting produced.</li>"
        "<li><strong>Pre-sleep wind-down</strong>: the body is still in sympathetic mode from the day's activities. The Reset shifts the nervous system toward parasympathetic before sleep.</li>"
        "<li><strong>Post-travel re-grounding</strong>: returning from a trip. The body is in unfamiliar proprioceptive territory. The Reset re-establishes the local sense of self.</li>"
        "</ol>",
        "<h3>Khi Nào Dùng Reset</h3>"
        "<p>Reset không phải thay thế cho thực hành. Đó là cầu nối giữa các thực hành &mdash; những gì bạn làm khi thực hành không có sẵn.</p>"
        "<p>Năm tình huống nơi Reset xứng đáng với tên gọi:</p>"
        "<ol>"
        "<li><strong>Sụp năng lượng giữa ngày</strong>: sự sụt giảm lúc 2 giờ chiều. Reset (đặc biệt thở Đan Điền) khôi phục trương lực phó giao cảm và nâng năng lượng mà không cần caffeine.</li>"
        "<li><strong>Bình tĩnh trước cuộc họp</strong>: một cuộc họp khó trong mười phút. Reset an định hơi thở và tâm để cuộc họp bắt đầu từ đường cơ sở bình tĩnh hơn.</li>"
        "<li><strong>Phục hồi sau cuộc họp</strong>: một cuộc họp khó vừa kết thúc. Reset giải phóng hưng phấn giao cảm mà cuộc họp tạo ra.</li>"
        "<li><strong>Giãn cơ trước khi ngủ</strong>: cơ thể vẫn ở chế độ giao cảm từ các hoạt động ban ngày. Reset chuyển hệ thần kinh về phó giao cảm trước khi ngủ.</li>"
        "<li><strong>Tái định vị sau du lịch</strong>: trở về từ một chuyến đi. Cơ thể ở lãnh thổ cảm giác bản thể lạ. Reset tái lập cảm giác bản thân địa phương.</li>"
        "</ol>",
    ),
    (
        "<h3>Why 60 Seconds Per Step</h3>"
        "<p>Each step in the Reset is 60 seconds. This duration is not arbitrary:</p>"
        "<ol>"
        "<li><strong>Short enough to do anywhere</strong>: 60 seconds is a small commitment. The body will agree to 60 seconds when it will not agree to 10 minutes.</li>"
        "<li><strong>Long enough to shift state</strong>: 60 seconds is enough time for the breath to deepen, for the spine to mobilise, for the shoulders to release. Shorter than 60 seconds, the shift is incomplete.</li>"
        "<li><strong>Round number, easy to count</strong>: 60 seconds requires no timer. Count breaths (5&ndash;10 slow breaths) or count repetitions (5&ndash;6 spinal rolls).</li>"
        "</ol>"
        "<p>The five steps are not a sequence to be performed perfectly. They are a menu. On some days, only step 1 is available. On other days, only step 4. Any single step, used alone, is itself a complete Reset.</p>",

        "<h3>Tại Sao 60 Giây Mỗi Bước</h3>"
        "<p>Mỗi bước trong Reset là 60 giây. Thời lượng này không ngẫu nhiên:</p>"
        "<ol>"
        "<li><strong>Đủ ngắn để làm ở bất cứ đâu</strong>: 60 giây là cam kết nhỏ. Cơ thể sẽ đồng ý 60 giây khi nó không đồng ý 10 phút.</li>"
        "<li><strong>Đủ dài để chuyển trạng thái</strong>: 60 giây là đủ thời gian để hơi thở sâu hơn, cột sống vận động, vai thả. Ngắn hơn 60 giây, sự chuyển dịch không đầy đủ.</li>"
        "<li><strong>Số tròn, dễ đếm</strong>: 60 giây không cần đồng hồ. Đếm hơi thở (5&ndash;10 hơi chậm) hoặc đếm lần lặp (5&ndash;6 cuộn cột sống).</li>"
        "</ol>"
        "<p>Năm bước không phải chuỗi được thực hiện hoàn hảo. Chúng là thực đơn. Một số ngày, chỉ bước 1 có sẵn. Những ngày khác, chỉ bước 4. Bất kỳ bước đơn lẻ nào, sử dụng riêng, tự nó là một Reset hoàn chỉnh.</p>",
    ),
]


BAY_SAI_LAM = [
    (
        "<h3>How These Sins Emerge</h3>"
        "<p>The seven sins are not random; they emerge predictably from common habits of the modern body:</p>"
        "<ol>"
        "<li><strong>Holding the breath</strong>: emerges from chronic stress (the body braces against the next demand).</li>"
        "<li><strong>Leading with the arms</strong>: emerges from upper-body-dominant work (typing, driving, lifting).</li>"
        "<li><strong>Locking the knees</strong>: emerges from a culture that treats standing as &ldquo;rigid posture&rdquo; rather than &ldquo;active alignment&rdquo;.</li>"
        "<li><strong>Puffing the chest</strong>: emerges from military and athletic training that emphasises chest-out posture.</li>"
        "<li><strong>Double-loading</strong>: emerges from the fear of imbalance (the body hedges against the possibility of falling).</li>"
        "<li><strong>Sinking the shoulders too far</strong>: emerges from misapplied &ldquo;relaxation&rdquo; instructions (the body drops rather than releases).</li>"
        "<li><strong>Moving the head before the body</strong>: emerges from a culture that uses the head/neck to &ldquo;look&rdquo; its way through space.</li>"
        "</ol>"
        "<p>Recognising where a sin comes from helps release it. The sin is not a personal failing; it is a learned pattern. Patterns can be unlearned.</p>",

        "<h3>Bảy Lỗi Này Nảy Sinh Như Thế Nào</h3>"
        "<p>Bảy lỗi không ngẫu nhiên; chúng nảy sinh có thể dự đoán từ các thói quen phổ biến của cơ thể hiện đại:</p>"
        "<ol>"
        "<li><strong>Nín thở</strong>: nảy sinh từ căng thẳng mãn tính (cơ thể chống lại nhu cầu tiếp theo).</li>"
        "<li><strong>Dẫn bằng tay</strong>: nảy sinh từ công việc thân trên chiếm ưu thế (gõ phím, lái xe, nâng).</li>"
        "<li><strong>Khóa gối</strong>: nảy sinh từ văn hóa coi đứng là &ldquo;tư thế cứng&rdquo; thay vì &ldquo;trục chủ động&rdquo;.</li>"
        "<li><strong>Phồng ngực</strong>: nảy sinh từ huấn luyện quân sự và thể thao nhấn mạnh tư thế ngực ra.</li>"
        "<li><strong>Song tải</strong>: nảy sinh từ nỗi sợ mất thăng bằng (cơ thể phòng vệ chống lại khả năng ngã).</li>"
        "<li><strong>Hạ vai quá sâu</strong>: nảy sinh từ các hướng dẫn &ldquo;thư giãn&rdquo; áp dụng sai (cơ thể rơi thay vì thả).</li>"
        "<li><strong>Di chuyển đầu trước thân</strong>: nảy sinh từ văn hóa dùng đầu/cổ để &ldquo;nhìn&rdquo; xuyên qua không gian.</li>"
        "</ol>"
        "<p>Nhận ra lỗi đến từ đâu giúp thả nó. Lỗi không phải thất bại cá nhân; đó là mẫu đã học. Các mẫu có thể bỏ học.</p>",
    ),
    (
        "<h3>When to Fix the Seventh Sin</h3>"
        "<p>The first six sins are addressable through daily practice. The seventh sin &mdash; moving the head before the body &mdash; is <em>not addressable through form practice alone</em>. It is a lifelong habit of perception, and the cure is to slow down <em>all of life</em>, not just the form.</p>"
        "<p>The form practice helps: it teaches the body to organise around the centre rather than the head. But the cure requires the form practice to be supported by everyday practices: walking slower, turning the head last when entering a room, eating without looking at the phone, sleeping with the head on the pillow rather than the phone under the pillow.</p>"
        "<p>The seventh sin is a life-style sin. Its cure is a life-style cure.</p>",

        "<h3>Khi Nào Sửa Lỗi Thứ Bảy</h3>"
        "<p>Sáu lỗi đầu tiên có thể giải quyết qua thực hành hằng ngày. Lỗi thứ bảy &mdash; di chuyển đầu trước thân &mdash; <em>không thể giải quyết chỉ qua thực hành bài quyền</em>. Đó là thói quen nhận thức suốt đời, và cách chữa là làm chậm lại <em>toàn bộ cuộc sống</em>, không chỉ bài quyền.</p>"
        "<p>Thực hành bài quyền giúp: nó dạy cơ thể tổ chức quanh trung tâm thay vì đầu. Nhưng cách chữa yêu cầu thực hành bài quyền được hỗ trợ bởi thực hành hằng ngày: đi bộ chậm hơn, quay đầu cuối cùng khi vào phòng, ăn không nhìn điện thoại, ngủ với đầu trên gối thay vì điện thoại dưới gối.</p>"
        "<p>Lỗi thứ bảy là lỗi lối sống. Cách chữa là cách chữa lối sống.</p>",
    ),
]


NGHICH_LY_CANG = [
    (
        "<h3>What the Science Says</h3>"
        "<p>Sports science has documented the fascia advantage in a series of studies since 2010. <strong>Tilp et al. (2016)</strong> showed that long, slow, full-range movements activate the fascia at a level that short, fast, partial movements do not. <strong>Schleip et al. (2019)</strong> showed that fascial activation is metabolically cheaper than muscular activation &mdash; the same force delivered costs less energy. <strong>Mersmann et al. (2021)</strong> showed that heavy weight training actually <em>reduces</em> fascial elasticity in some regions, while long, slow movement increases it.</p>"
        "<p>These findings validate what Tai Chi practitioners have always known: the slow form is not a beginner&rsquo;s form. It is the master&rsquo;s form. It is slow because slow is the speed at which the fascia works best.</p>",

        "<h3>Khoa Học Nói Gì</h3>"
        "<p>Khoa học thể thao đã ghi nhận lợi thế cân mạc trong một loạt nghiên cứu từ 2010. <strong>Tilp và cs. (2016)</strong> cho thấy chuyển động dài, chậm, toàn phạm vi kích hoạt cân mạc ở mức mà chuyển động ngắn, nhanh, một phần không làm được. <strong>Schleip và cs. (2019)</strong> cho thấy kích hoạt cân mạc rẻ hơn về trao đổi chất so với kích hoạt cơ bắp &mdash; cùng lực được tạo ra tốn ít năng lượng hơn. <strong>Mersmann và cs. (2021)</strong> cho thấy tập tạ nặng thực sự <em>giảm</em> đàn hồi cân mạc ở một số vùng, trong khi chuyển động dài, chậm tăng nó.</p>"
        "<p>Những phát hiện này xác nhận những gì người tập Thái Cực Quyền luôn biết: bài quyền chậm không phải bài quyền của người mới. Đó là bài quyền của bậc thầy. Nó chậm vì chậm là tốc độ mà cân mạc hoạt động tốt nhất.</p>",
    ),
    (
        "<h3>Why Strong Muscles Make Weak Tai Chi</h3>"
        "<p>The mechanism: when a muscle contracts strongly, it stiffens. When the surrounding muscle group is also contracted strongly, the entire region stiffens. When the entire region is stiff, the fascia beneath cannot move freely. The fascia becomes a passive bystander in a muscular event it should have driven.</p>"
        "<p>Tai Chi requires the fascia to be an active participant. For the fascia to participate, the muscles must be relaxed enough that the fascia has room to lengthen and shorten. Strong, constantly-engaged muscles steal this room. The result: a body that is strong by gym standards but weak by Tai Chi standards.</p>"
        "<p>The fix is not to weaken the muscles. It is to <em>educate</em> them &mdash; to teach them to engage only when needed and to release when not. This is what Tai Chi practice does.</p>",

        "<h3>Tại Sao Cơ Bắp Mạnh Tạo Thái Cực Yếu</h3>"
        "<p>Cơ chế: khi một cơ co mạnh, nó cứng lại. Khi nhóm cơ xung quanh cũng co mạnh, toàn bộ vùng cứng lại. Khi toàn bộ vùng cứng, cân mạc bên dưới không thể di chuyển tự do. Cân mạc trở thành khán giả thụ động trong một sự kiện cơ bắp mà nó nên lái.</p>"
        "<p>Thái Cực Quyền yêu cầu cân mạc là người tham gia tích cực. Để cân mạc tham gia, cơ bắp phải đủ thư giãn để cân mạc có không gian dài ra và rút ngắn. Cơ bắp mạnh, liên tục gắn kết, lấy không gian này. Kết quả: một cơ thể mạnh theo tiêu chuẩn gym nhưng yếu theo tiêu chuẩn Thái Cực.</p>"
        "<p>Cách sửa không phải là yếu cơ bắp đi. Đó là <em>giáo dục</em> chúng &mdash; dạy chúng chỉ gắn kết khi cần và thả khi không. Đây là điều thực hành Thái Cực Quyền làm.</p>",
    ),
]


TAICHI_LA_GI = [
    (
        "<h3>What the Slow Form Hides</h3>"
        "<p>From the outside, the slow form looks like a public park demonstration. From the inside, the slow form is one of the most cognitively demanding activities available to a human being. The brain must simultaneously: maintain structural integration, coordinate breath with movement, track the location of weight, attend to nine checkpoints, manage the emotional state, observe the form without judging, and stay present without grasping.</p>"
        "<p>This is why a 30-minute slow form produces more learning than a 10-minute fast form. The cognitive bandwidth required is enormous; the slow pace allows the brain to allocate that bandwidth without being overwhelmed. Faster practice would hide the cognitive demand under the muscular demand.</p>",

        "<h3>Bài Quyền Chậm Giấu Gì</h3>"
        "<p>Từ bên ngoài, bài quyền chậm trông giống biểu diễn công viên. Từ bên trong, bài quyền chậm là một trong những hoạt động đòi hỏi nhận thức nhất có sẵn cho con người. Não phải đồng thời: duy trì tích hợp cấu trúc, phối hợp hơi thở với chuyển động, theo dõi vị trí trọng lượng, chú ý đến chín điểm, quản lý trạng thái cảm xúc, quan sát bài quyền mà không phán xét, và giữ hiện diện mà không nắm bắt.</p>"
        "<p>Đây là lý do bài quyền chậm 30 phút tạo ra nhiều học hơn bài quyền nhanh 10 phút. Băng thông nhận thức cần thiết rất lớn; nhịp độ chậm cho phép não phân bổ băng thông đó mà không bị choáng ngợp. Thực hành nhanh hơn sẽ giấu nhu cầu nhận thức dưới nhu cầu cơ bắp.</p>",
    ),
    (
        "<h3>What Tai Chi Is Not</h3>"
        "<p>To know what Tai Chi is, it helps to know what it is not:</p>"
        "<ul>"
        "<li><strong>Not a dance</strong>: the form is choreographed, but the choreography serves internal organisation, not aesthetic display. No external audience is needed.</li>"
        "<li><strong>Not a martial art in the popular sense</strong>: Tai Chi does not teach violence. It teaches how to meet force with structure, not how to initiate force. Most Tai Chi practitioners never engage in combat; the martial origin is a training methodology, not an application.</li>"
        "<li><strong>Not a religion</strong>: Tai Chi draws from Daoism and Buddhism but is not itself a religion. The practice works whether the practitioner holds any belief or none.</li>"
        "<li><strong>Not a therapy</strong>: although Tai Chi has documented therapeutic benefits, it is not primarily a therapy. The benefits come from a practice that has its own integrity; using Tai Chi as a therapy underestimates what it is.</li>"
        "<li><strong>Not a meditation in the popular sense</strong>: Tai Chi involves movement, so it does not look like sitting meditation. But the depth of concentration it requires is comparable to sitting meditation; the two are different forms of the same underlying practice.</li>"
        "</ul>",
        "<h3>Thái Cực Quyền Không Phải Là Gì</h3>"
        "<p>Để biết Thái Cực Quyền là gì, giúp biết nó không phải là gì:</p>"
        "<ul>"
        "<li><strong>Không phải múa</strong>: bài quyền được biên đạo, nhưng biên đạo phục vụ tổ chức nội tại, không phải trình diễn thẩm mỹ. Không cần khán giả bên ngoài.</li>"
        "<li><strong>Không phải võ thuật theo nghĩa phổ biến</strong>: Thái Cực Quyền không dạy bạo lực. Nó dạy cách gặp lực bằng cấu trúc, không phải cách khởi phát lực. Hầu hết người tập Thái Cực Quyền không bao giờ tham gia chiến đấu; nguồn gốc võ thuật là phương pháp huấn luyện, không phải ứng dụng.</li>"
        "<li><strong>Không phải tôn giáo</strong>: Thái Cực Quyền rút từ Đạo giáo và Phật giáo nhưng không tự nó là tôn giáo. Thực hành có hiệu quả cho dù người tập có bất kỳ niềm tin nào hay không.</li>"
        "<li><strong>Không phải trị liệu</strong>: mặc dù Thái Cực Quyền có lợi ích trị liệu được ghi nhận, nó không chủ yếu là trị liệu. Lợi ích đến từ thực hành có tính toàn vẹn riêng; dùng Thái Cực Quyền như trị liệu đánh giá thấp nó là gì.</li>"
        "<li><strong>Không phải thiền theo nghĩa phổ biến</strong>: Thái Cực Quyền liên quan đến chuyển động, nên nó không trông giống thiền ngồi. Nhưng độ sâu tập trung nó yêu cầu tương đương với thiền ngồi; cả hai là hình thức khác nhau của cùng thực hành nền tảng.</li>"
        "</ul>",
    ),
]


TAM_BAO = [
    (
        "<h3>What Each Treasure Feels Like</h3>"
        "<p>The Three Treasures are not abstractions. They are felt experiences, each with a distinctive signature:</p>"
        "<ol>"
        "<li><strong>Jīng (精)</strong>: felt in the lower abdomen and the lower back. The signature is a sense of <em>substantial weight</em> &mdash; the body feels denser, more present. The breath sits deeper. The pelvis is heavy. Jīng is the body&rsquo;s experience of its own materiality.</li>"
        "<li><strong>Qì (氣)</strong>: felt as warmth and flow. The signature is <em>movement without obvious source</em> &mdash; a sensation that something is circulating, but the body cannot identify which muscle is producing it. Qì is the body&rsquo;s experience of its own aliveness.</li>"
        "<li><strong>Shén (神)</strong>: felt in the eyes and the mind. The signature is <em>presence without effort</em> &mdash; the gaze is awake, the mind is clear, but neither is being driven. Shén is the body&rsquo;s experience of its own awareness.</li>"
        "</ol>",
        "<h3>Mỗi Bảo Cảm Thấy Như Thế Nào</h3>"
        "<p>Tam Bảo không phải trừu tượng. Chúng là trải nghiệm được cảm nhận, mỗi cái có một đặc trưng riêng biệt:</p>"
        "<ol>"
        "<li><strong>Tinh (精)</strong>: cảm nhận ở bụng dưới và lưng dưới. Đặc trưng là cảm giác <em>trọng lượng chắc chắn</em> &mdash; cơ thể cảm thấy đặc hơn, hiện diện hơn. Hơi thở ngồi sâu hơn. Khung chậu nặng. Tinh là trải nghiệm của cơ thể về tính chất vật chất của chính nó.</li>"
        "<li><strong>Khí (氣)</strong>: cảm nhận như hơi ấm và dòng chảy. Đặc trưng là <em>chuyển động không có nguồn rõ ràng</em> &mdash; cảm giác rằng cái gì đó đang lưu thông, nhưng cơ thể không thể xác định cơ nào đang tạo ra nó. Khí là trải nghiệm của cơ thể về sự sống của chính nó.</li>"
        "<li><strong>Thần (神)</strong>: cảm nhận ở mắt và tâm. Đặc trưng là <em>hiện diện không cố gắng</em> &mdash; ánh mắt tỉnh, tâm trong, nhưng không cái nào bị thúc đẩy. Thần là trải nghiệm của cơ thể về ý thức của chính nó.</li>"
        "</ol>",
    ),
    (
        "<h3>How the Treasures Refine Each Other</h3>"
        "<p>The refinement is bidirectional, not just linear. Just as Jīng refines into Qì and Qì into Shén, so does Shén support Jīng and Qì. A clear mind (Shén) helps preserve essence (Jīng). Preserved essence produces smoother Qì. Smoother Qì supports clearer Shén. The cycle strengthens itself.</p>"
        "<p>Most beginners experience the linear direction only: they feel <em>more alive</em> (Qì) but cannot articulate it; they feel <em>more present</em> (Shén) but cannot sustain it; they feel <em>heavier</em> (Jīng) but cannot integrate it. With daily practice over months, the cycle begins to integrate. The treasures stop being separate experiences and become a single felt sense: <em>this body, this mind, this moment</em>.</p>",

        "<h3>Các Bảo Tinh Luyện Lẫn Nhau</h3>"
        "<p>Sự tinh luyện là hai chiều, không chỉ tuyến tính. Cũng như Tinh tinh luyện thành Khí và Khí thành Thần, Thần cũng hỗ trợ Tinh và Khí. Một tâm trong (Thần) giúp bảo tồn tinh hoa (Tinh). Tinh hoa được bảo tồn tạo ra Khí mượt hơn. Khí mượt hơn hỗ trợ Thần trong hơn. Chu kỳ tự củng cố.</p>"
        "<p>Hầu hết người mới chỉ trải nghiệm hướng tuyến tính: họ cảm thấy <em>sống hơn</em> (Khí) nhưng không thể diễn đạt; họ cảm thấy <em>hiện diện hơn</em> (Thần) nhưng không thể duy trì; họ cảm thấy <em>nặng hơn</em> (Tinh) nhưng không thể tích hợp. Với thực hành hằng ngày qua nhiều tháng, chu kỳ bắt đầu tích hợp. Các bảo ngừng là trải nghiệm riêng biệt và trở thành một cảm giác đơn nhất: <em>cơ thể này, tâm này, khoảnh khắc này</em>.</p>",
    ),
]


AM_DUONG = [
    (
        "<h3>The Eight Trigrams (Bāguà 八卦)</h3>"
        "<p>The I Ching (易经) extends Yin-Yang into a system of eight trigrams: <strong>Qián ☰</strong> (Heaven, pure Yang), <strong>Duì ☱</strong> (Lake, Yang), <strong>Lí ☲</strong> (Fire, Yang), <strong>Zhèn ☳</strong> (Thunder, Yang), <strong>Xún ☴</strong> (Wind, Yin), <strong>Kǎn ☵</strong> (Water, Yin), <strong>Gèn ☶</strong> (Mountain, Yin), <strong>Kūn ☷</strong> (Earth, pure Yin). Each trigram has three lines; Yang lines are solid (—), Yin lines are broken (- -).</p>"
        "<p>The eight trigrams combine into 64 hexagrams (six-line combinations). The I Ching uses these 64 configurations to describe every possible state of any process. Tai Chi uses them implicitly: each movement has a trigram-like configuration of Yin and Yang, and transitions between movements follow the logic of trigram change.</p>",

        "<h3>Bát Quái (八卦)</h3>"
        "<p>Kinh Dịch mở rộng Âm Dương thành hệ thống tám quái: <strong>Càn ☰</strong> (Trời, Dương thuần), <strong>Đoài ☱</strong> (Hồ, Dương), <strong>Ly ☲</strong> (Hỏa, Dương), <strong>Chấn ☳</strong> (Sấm, Dương), <strong>Tốn ☴</strong> (Phong, Âm), <strong>Khảm ☵</strong> (Thủy, Âm), <strong>Cấn ☶</strong> (Sơn, Âm), <strong>Khôn ☷</strong> (Đất, Âm thuần). Mỗi quái có ba hào; hào Dương là liền (—), hào Âm là đứt (- -).</p>"
        "<p>Tám quái kết hợp thành 64 quẻ (kết hợp sáu hào). Kinh Dịch dùng 64 cấu hình này để mô tả mọi trạng thái có thể của bất kỳ quá trình nào. Thái Cực Quyền sử dụng chúng ngầm: mỗi chuyển động có cấu hình giống quái của Âm và Dương, và sự chuyển tiếp giữa các chuyển động theo logic thay đổi quái.</p>",
    ),
    (
        "<h3>The Five Elements (Wǔ Xíng 五行)</h3>"
        "<p>A second extension: Yin-Yang plus the eight trigrams gives 64 combinations, but the practical application in Chinese medicine uses a simpler five-element system: <strong>Wood</strong> (growth, expansion), <strong>Fire</strong> (flame, rising), <strong>Earth</strong> (stability, transformation), <strong>Metal</strong> (contraction, clarity), <strong>Water</strong> (descent, storage). Each element generates the next (Wood feeds Fire, Fire creates Earth, Earth bears Metal, Metal collects Water, Water nourishes Wood) and controls the next (Wood parts Earth, Earth absorbs Water, Water quenches Fire, Fire melts Metal, Metal cuts Wood).</p>"
        "<p>Tai Chi is sometimes described as &ldquo;Wood-Fire-Earth-Metal-Water applied to the body&rdquo;. Each element corresponds to a state of the body&rsquo;s energy: Wood is the opening of a movement; Fire is the peak of a movement; Earth is the centre of a movement; Metal is the closing of a movement; Water is the descent before the next movement. The form cycles through the elements continuously.</p>",

        "<h3>Ngũ Hành (五行)</h3>"
        "<p>Một mở rộng thứ hai: Âm Dương cộng tám quái cho 64 kết hợp, nhưng ứng dụng thực tế trong y học Trung Hoa dùng hệ thống ngũ hành đơn giản hơn: <strong>Mộc</strong> (tăng trưởng, mở rộng), <strong>Hỏa</strong> (ngọn lửa, dâng lên), <strong>Thổ</strong> (ổn định, chuyển hóa), <strong>Kim</strong> (co lại, trong sáng), <strong>Thủy</strong> (hạ xuống, lưu trữ). Mỗi hành sinh ra hành tiếp theo (Mộc nuôi Hỏa, Hỏa tạo Thổ, Thổ sinh Kim, Kim thu Thủy, Thủy dưỡng Mộc) và khắc hành tiếp theo (Mộc phá Thổ, Thổ hấp thụ Thủy, Thủy dập Hỏa, Hỏa nấu Kim, Kim cắt Mộc).</p>"
        "<p>Thái Cực Quyền đôi khi được mô tả là &ldquo;Mộc-Hỏa-Thổ-Kim-Thủy áp dụng cho cơ thể&rdquo;. Mỗi hành tương ứng với một trạng thái năng lượng của cơ thể: Mộc là sự mở đầu của chuyển động; Hỏa là đỉnh của chuyển động; Thổ là trung tâm của chuyển động; Kim là sự đóng của chuyển động; Thủy là sự hạ trước chuyển động tiếp theo. Bài quyền luân phiên qua các hành liên tục.</p>",
    ),
]


SO_DO_CO_THE = [
    (
        "<h3>Why Three and Not One</h3>"
        "<p>A single map can become a fixation. Beginners who only track weight often forget breath; beginners who only track breath often forget alignment. The three maps work together to keep the whole body present.</p>"
        "<p>The maps also have different timescales. <strong>Weight</strong> changes every second &mdash; it is the fastest map. <strong>Alignment</strong> changes every few minutes &mdash; it is the slowest map. <strong>Ground</strong> changes every step &mdash; it is intermediate. The three timescales nest inside each other, which is why all three need attention.</p>",
        "<h3>Tại Sao Ba Mà Không Phải Một</h3>"
        "<p>Một bản đồ duy nhất có thể trở thành sự cố định. Người mới chỉ theo dõi trọng lượng thường quên hơi thở; người mới chỉ theo dõi hơi thở thường quên trục. Ba bản đồ làm việc cùng nhau để giữ toàn bộ cơ thể hiện diện.</p>"
        "<p>Các bản đồ cũng có thang thời gian khác nhau. <strong>Trọng lượng</strong> thay đổi mỗi giây &mdash; đó là bản đồ nhanh nhất. <strong>Trục</strong> thay đổi vài phút một lần &mdash; đó là bản đồ chậm nhất. <strong>Mặt đất</strong> thay đổi mỗi bước &mdash; đó là bản đồ trung gian. Ba thang thời gian lồng vào nhau, đó là lý do cả ba cần chú ý.</p>",
    ),
    (
        "<h3>How the Maps Combine in a Single Movement</h3>"
        "<p>Take Commencing Form (Khởi Thức). The arms rise as the breath descends (weight map: weight sinks; ground map: feet press evenly; alignment map: spine lengthens). Three maps, three instructions, all happening simultaneously.</p>"
        "<p>Take Single Whip (Đơn Tiên). The weight shifts right as the arms open left (weight map: weight moves right; ground map: left foot lightens, right foot presses; alignment map: spine turns slightly right). Three maps, three instructions, all happening simultaneously.</p>"
        "<p>Take Cloud Hands (Vân Thủ). The weight shifts side to side (weight map: weight traces a horizontal line; ground map: feet alternate pressing; alignment map: spine stays vertical). Three maps, three instructions, all happening simultaneously.</p>",

        "<h3>Các Bản Đồ Kết Hợp Trong Một Chuyển Động</h3>"
        "<p>Lấy Khởi Thức. Tay nâng lên khi hơi thở đi xuống (bản đồ trọng lượng: trọng lượng chìm; bản đồ mặt đất: chân ấn đều; bản đồ trục: cột sống dài ra). Ba bản đồ, ba chỉ dẫn, tất cả xảy ra đồng thời.</p>"
        "<p>Lấy Đơn Tiên. Trọng lượng chuyển phải khi tay mở trái (bản đồ trọng lượng: trọng lượng di chuyển phải; bản đồ mặt đất: chân trái nhẹ, chân phải ấn; bản đồ trục: cột sống xoay nhẹ phải). Ba bản đồ, ba chỉ dẫn, tất cả xảy ra đồng thời.</p>"
        "<p>Lấy Vân Thủ. Trọng lượng chuyển sang bên (bản đồ trọng lượng: trọng lượng vẽ đường ngang; bản đồ mặt đất: chân luân phiên ấn; bản đồ trục: cột sống giữ thẳng đứng). Ba bản đồ, ba chỉ dẫn, tất cả xảy ra đồng thời.</p>",
    ),
]


VO_VI_TRU_THE = [
    (
        "<h3>The Wandering Mind as Practice</h3>"
        "<p>The wandering mind is not a problem to solve; it is the practice itself. Each wandering is a chance to notice. Each noticing is a chance to return. Each return is a micro-repetition of the entire meditation cycle.</p>"
        "<p>This is why &ldquo;trying to stop thinking&rdquo; is the wrong approach. The mind cannot be commanded to stop; it can only be invited to notice. The noticing happens repeatedly, gently, without judgment. Over time, the noticings become faster and the wanderings become shorter. The meditation is not the stillness between wanderings; the meditation is the noticing of the wanderings.</p>",

        "<h3>Tâm Lang Thang Như Thực Hành</h3>"
        "<p>Tâm lang thang không phải vấn đề cần giải quyết; đó chính là thực hành. Mỗi lần lang thang là cơ hội để nhận ra. Mỗi lần nhận ra là cơ hội để trở lại. Mỗi lần trở lại là một lần lặp lại vi mô của toàn bộ chu kỳ thiền.</p>"
        "<p>Đây là lý do &ldquo;cố ngừng suy nghĩ&rdquo; là cách tiếp cận sai. Tâm không thể bị ra lệnh dừng; nó chỉ có thể được mời gọi nhận ra. Sự nhận ra xảy ra lặp đi lặp lại, nhẹ nhàng, không phán xét. Theo thời gian, sự nhận ra trở nên nhanh hơn và sự lang thang trở nên ngắn hơn. Thiền không phải sự tĩnh lặng giữa các lần lang thang; thiền là sự nhận ra các lần lang thang.</p>",
    ),
    (
        "<h3>When Standing Becomes Moving</h3>"
        "<p>The most advanced Zhan Zhuang practice is invisible: the practitioner stands, and then begins to move, without any visible transition. The standing posture and the moving form merge into one continuous practice.</p>"
        "<p>This is the long-term destination of Zhan Zhuang. The five-minute standing is preparation. The thirty-minute standing is integration. The merged standing-and-moving is mastery. Each stage takes years to develop; most practitioners spend most of their years in the preparation stage, and that is appropriate. The preparation itself produces results that justify the years.</p>",

        "<h3>Khi Trụ Thế Trở Thành Chuyển Động</h3>"
        "<p>Thực hành Trụ Thế nâng cao nhất là vô hình: người tập đứng, và sau đó bắt đầu di chuyển, không có sự chuyển tiếp nào nhìn thấy được. Tư thế đứng và bài quyền hợp nhất thành một thực hành liên tục.</p>"
        "<p>Đây là đích dài hạn của Trụ Thế. Năm phút đứng là chuẩn bị. Ba mươi phút đứng là tích hợp. Sự hợp nhất đứng-và-di-chuyển là thành thạo. Mỗi giai đoạn mất nhiều năm để phát triển; hầu hết người tập dành phần lớn năm của họ ở giai đoạn chuẩn bị, và điều đó thích hợp. Bản thân sự chuẩn bị tạo ra kết quả biện minh cho nhiều năm.</p>",
    ),
]


LAY = [
    (
        "<h3>Rollback vs Escape</h3>"
        "<p>Many students confuse Lu (Rollback) with <em>escape</em>. They see the sideways yielding and interpret it as &ldquo;running away.&rdquo; But Lu is not escape; it is <em>redirection</em>. The difference:</p>"
        "<ul>"
        "<li><strong>Escape</strong>: the opponent attacks; I retreat. Their force is still on target; they will pursue. I have used energy to retreat; they have used energy to attack. The energy exchange favours them.</li>"
        "<li><strong>Rollback</strong>: the opponent attacks; I yield sideways in the direction of their force. Their force follows the curve; their momentum carries them past their base. I have used no energy to retreat; they have used their own energy against themselves. The energy exchange favours me.</li>"
        "</ul>"
        "<p>The visible difference: escape looks like a step back; rollback looks like a step sideways followed by a step forward. Escape has no follow-up; rollback sets up the next technique.</p>",

        "<h3>Lãy vs Thoát</h3>"
        "<p>Nhiều học viên nhầm lẫn Lãy (Rollback) với <em>thoát</em>. Họ thấy sự nhường sang bên và diễn giải nó là &ldquo;chạy trốn.&rdquo; Nhưng Lãy không phải thoát; đó là <em>chuyển hướng</em>. Sự khác biệt:</p>"
        "<ul>"
        "<li><strong>Thoát</strong>: đối phương tấn công; tôi rút lui. Lực của họ vẫn nhắm đích; họ sẽ đuổi theo. Tôi đã dùng năng lượng để rút lui; họ đã dùng năng lượng để tấn công. Trao đổi năng lượng có lợi cho họ.</li>"
        "<li><strong>Lãy</strong>: đối phương tấn công; tôi nhường sang bên theo hướng lực của họ. Lực của họ theo đường cong; quán tính của họ mang họ qua căn cứ. Tôi không dùng năng lượng để rút lui; họ đã dùng năng lượng của chính họ chống lại chính họ. Trao đổi năng lượng có lợi cho tôi.</li>"
        "</ul>"
        "<p>Sự khác biệt nhìn thấy được: thoát trông giống bước lùi; lãy trông giống bước sang bên theo sau bằng bước tới. Thoát không có tiếp theo; lãy thiết lập kỹ thuật tiếp theo.</p>",
    ),
    (
        "<h3>Where Lu Meets Tui Shou (Push Hands)</h3>"
        "<p>Push hands (Tôi Thủ) is where Lu is internalised. Two practitioners in contact, taking turns attacking and yielding. The attacker pushes; the defender applies Lu. The defender redirects the attack back toward the attacker; the attacker becomes the defender. The cycle continues.</p>"
        "<p>The most valuable Push Hands insight is that Lu does not require a strong attack to be visible. A gentle push reveals Lu clearly; a strong push obscures Lu (because the defender must add force to redirect). This is why senior practitioners Push Hands slowly: slow force reveals structure; fast force hides it.</p>",

        "<h3>Nơi Lãy Gặp Tôi Thủ</h3>"
        "<p>Tôi Thủ là nơi Lãy được nội tâm hóa. Hai người tập tiếp xúc, luân phiên tấn công và nhường. Người tấn công đẩy; người phòng thủ áp dụng Lãy. Người phòng thủ chuyển hướng cuộc tấn công trở lại người tấn công; người tấn công trở thành người phòng thủ. Chu kỳ tiếp tục.</p>"
        "<p>Thông tin chi tiết có giá trị nhất của Tôi Thủ là Lãy không cần cuộc tấn công mạnh để nhìn thấy được. Một cú đẩy nhẹ tiết lộ Lãy rõ ràng; một cú đẩy mạnh che Lãy (vì người phòng thủ phải thêm lực để chuyển hướng). Đây là lý do người tập cao cấp Tôi Thủ chậm: lực chậm tiết lộ cấu trúc; lực nhanh che nó.</p>",
    ),
]


TWENTY_FOUR_THUC_TONG_QUAT = [
    (
        "<h3>The Three Internal Methods in the 24-Form</h3>"
        "<p>The 24-Form teaches three internal methods simultaneously. Most students notice the form&rsquo;s external choreography but not the internal methods running underneath.</p>"
        "<ol>"
        "<li><strong>Yì Dǎo (意导) — intention leads</strong>: every movement begins with an intention. The intention forms in the mind, then the body follows. Watch a senior practitioner: the movement seems to start in the eyes before it starts in the arms.</li>"
        "<li><strong>Qì Dǎo (气导) — breath leads</strong>: every movement is paired with breath. Inhale during opening movements; exhale during closing movements. Watch a senior practitioner: the breath is audible but never forced.</li>"
        "<li><strong>Lì Dǎo (力导) — structure leads</strong>: every movement arises from the structure (root, waist, spine, shoulders). The arms appear to move but they are being moved by the structure. Watch a senior practitioner: the arms look relaxed but the structure behind them is integrated.</li>"
        "</ol>",
        "<h3>Ba Phương Pháp Nội Tâm Trong 24 Thức</h3>"
        "<p>24 Thức dạy ba phương pháp nội tâm đồng thời. Hầu hết học viên nhận thấy biên đạo bên ngoài của bài quyền nhưng không nhận ra các phương pháp nội tâm chạy bên dưới.</p>"
        "<ol>"
        "<li><strong>Ý Dẫn (意导)</strong>: mọi chuyển động bắt đầu bằng ý định. Ý định hình thành trong tâm, sau đó cơ thể theo. Quan sát người tập cao cấp: chuyển động dường như bắt đầu ở mắt trước khi bắt đầu ở tay.</li>"
        "<li><strong>Khí Dẫn (气导)</strong>: mọi chuyển động được ghép với hơi thở. Hít vào trong các chuyển động mở; thở ra trong các chuyển động đóng. Quan sát người tập cao cấp: hơi thở nghe được nhưng không bao giờ bị ép.</li>"
        "<li><strong>Lực Dẫn (力导)</strong>: mọi chuyển động nảy sinh từ cấu trúc (căn, eo, cột sống, vai). Tay dường như di chuyển nhưng chúng đang được cấu trúc di chuyển. Quan sát người tập cao cấp: tay trông thư giãn nhưng cấu trúc phía sau chúng được tích hợp.</li>"
        "</ol>",
    ),
    (
        "<h3>Why 24 and Not 12 or 48</h3>"
        "<p>Some traditions teach a 12-form (minimum viable form). Some teach a 48-form (the Beijing Competition form). The 24-form is the middle path:</p>"
        "<ul>"
        "<li><strong>vs 12-form</strong>: 24 covers the 8 Gates more thoroughly. Each Gate (Peng, Lu, Ji, An, Cai, Lie, Zhou, Kao) appears at least once with multiple variations. The 12-form covers only the basic 4 (Peng, Lu, Ji, An).</li>"
        "<li><strong>vs 48-form</strong>: 24 is learnable in months; 48 is learnable in years. For most students, the 24-form provides enough complexity to occupy years of refinement, without requiring years of memorisation.</li>"
        "</ul>"
        "<p>The 24-form is a <em>gateway</em> form: small enough to learn, large enough to study forever.</p>",

        "<h3>Tại Sao 24 Mà Không Phải 12 Hay 48</h3>"
        "<p>Một số truyền thống dạy bài 12 thức (bài tối thiểu khả thi). Một số dạy bài 48 (bài thi đấu Bắc Kinh). 24 thức là con đường giữa:</p>"
        "<ul>"
        "<li><strong>so với 12 thức</strong>: 24 bao gồm Bát Môn kỹ lưỡng hơn. Mỗi Môn (Phòng, Lỹ, Tỳ, Án, Thái, Liệt, Chửu, Kháo) xuất hiện ít nhất một lần với nhiều biến thể. 12 thức chỉ bao gồm 4 cơ bản (Phòng, Lỹ, Tỳ, Án).</li>"
        "<li><strong>so với 48 thức</strong>: 24 có thể học trong vài tháng; 48 có thể học trong nhiều năm. Đối với hầu hết học viên, 24 thức cung cấp đủ phức tạp để chiếm nhiều năm tinh chỉnh, mà không yêu cầu nhiều năm ghi nhớ.</li>"
        "</ul>"
        "<p>24 thức là bài quyền <em>cổng</em>: đủ nhỏ để học, đủ lớn để nghiên cứu mãi mãi.</p>",
    ),
]


THO_DAN_DIEN = [
    (
        "<h3>The Dantian as Physical Location</h3>"
        "<p>The dantian is often described in mystical terms, but it has a concrete anatomical correlate. The <strong>lower dantian</strong> is the area roughly 3 cm below the navel, deep inside the pelvis, between the sacrum and the pubic symphysis. This area contains:</p>"
        "<ul>"
        "<li>the solar plexus (celiac ganglion), a major nerve centre for the abdominal organs;</li>"
        "<li>the root of the mesenteric arteries, supplying blood to the digestive tract;</li>"
        "<li>the insertion point of the psoas major, a deep hip flexor that connects the spine to the legs;</li>"
        "<li>a dense network of fascia that connects the diaphragm, the pelvic floor, and the deep abdominal muscles.</li>"
        "</ul>"
        "<p>Breathing into this area is not mystical. It is biomechanical: it massages the viscera, regulates intra-abdominal pressure, and activates the parasympathetic nervous system through the vagus nerve.</p>",

        "<h3>Đan Điền Như Vị Trí Vật Lý</h3>"
        "<p>Đan Điền thường được mô tả bằng các thuật ngữ thần bí, nhưng nó có một tương quan giải phẫu cụ thể. <strong>Đan Điền dưới</strong> là vùng khoảng 3 cm dưới rốn, sâu trong khung chậu, giữa xương cụt và khớp mu. Vùng này chứa:</p>"
        "<ul>"
        "<li>đám rối mặt trời (hạch tạng), một trung tâm thần kinh lớn cho các cơ quan bụng;</li>"
        "<li>gốc của các động mạch mạc treo, cung cấp máu cho đường tiêu hóa;</li>"
        "<li>điểm chèn của cơ thắt lưng lớn (psoas major), cơ gập hông sâu kết nối cột sống với chân;</li>"
        "<li>mạng lưới cân mạc dày đặc kết nối cơ hoành, sàn chậu, và các cơ bụng sâu.</li>"
        "</ul>"
        "<p>Thở vào vùng này không phải thần bí. Nó là cơ sinh học: nó xoa bóp các tạng, điều hòa áp suất trong bụng, và kích hoạt hệ thần kinh phó giao cảm qua dây thần kinh phế vị.</p>",
    ),
    (
        "<h3>Why Belly Breathing Calms the Mind</h3>"
        "<p>Two pathways:</p>"
        "<ol>"
        "<li><strong>Vagal pathway</strong>: slow, deep breathing stimulates the vagus nerve, which runs from the brainstem through the neck and into the abdomen. Vagal stimulation activates the parasympathetic nervous system &mdash; the &ldquo;rest and digest&rdquo; mode. Heart rate slows. Blood pressure drops. The stress hormones cortisol and adrenaline decrease.</li>"
        "<li><strong>Diaphragm pathway</strong>: deep belly breathing uses the diaphragm fully, which mechanically massages the vagus nerve as it passes through the diaphragm&rsquo;s opening (the aortic hiatus). Each breath is a small vagal massage.</li>"
        "</ol>"
        "<p>Both pathways converge on the same result: the nervous system shifts from sympathetic (fight-or-flight) to parasympathetic (rest-and-digest). The mind follows the body. The body&rsquo;s shift to parasympathetic produces the mind&rsquo;s shift to calm.</p>",

        "<h3>Tại Sao Thở Bụng Làm Tâm Bình Tĩnh</h3>"
        "<p>Hai con đường:</p>"
        "<ol>"
        "<li><strong>Con đường phế vị</strong>: thở chậm, sâu kích thích dây thần kinh phế vị, chạy từ thân não qua cổ và vào bụng. Kích thích phế vị kích hoạt hệ thần kinh phó giao cảm &mdash; chế độ &ldquo;nghỉ và tiêu hóa&rdquo;. Nhịp tim chậm. Huyết áp giảm. Hormone căng thẳng cortisol và adrenaline giảm.</li>"
        "<li><strong>Con đường cơ hoành</strong>: thở bụng sâu dùng cơ hoành đầy đủ, cơ học xoa bóp dây thần kinh phế vị khi nó đi qua lỗ cơ hoành (lỗ động mạch chủ). Mỗi hơi thở là một massage phế vị nhỏ.</li>"
        "</ol>"
        "<p>Cả hai con đường hội tụ ở cùng kết quả: hệ thần kinh chuyển từ giao cảm (chiến đấu-hay-chạy) sang phó giao cảm (nghỉ-và-tiêu hóa). Tâm theo cơ thể. Sự chuyển của cơ thể sang phó giao cảm tạo ra sự chuyển của tâm sang bình tĩnh.</p>",
    ),
]


BA_MO_NEO = [
    (
        "<h3>How to Use the Anchors Mid-Form</h3>"
        "<p>The 3-Anchor Check is not just for sitting or standing. It is for any moment when the practice feels off. Mid-form, when the movement becomes mechanical or distracted, the check has three quick questions:</p>"
        "<ol>"
        "<li><strong>Where is my weight?</strong> The answer should be precise (e.g., &ldquo;70% on the right foot&rdquo;). If you cannot answer precisely, weight is somewhere you have not noticed.</li>"
        "<li><strong>Where is my breath?</strong> The answer should be a specific location (e.g., &ldquo;low in the dantian&rdquo;). If breath is high in the chest, the practice has lost its grounding.</li>"
        "<li><strong>Where is my intention?</strong> The answer should be present-tense (e.g., &ldquo;on this movement&rdquo;). If intention is on the next movement or on the past, the practice has lost its presence.</li>"
        "</ol>"
        "<p>The check takes five seconds. It does not interrupt the practice; it deepens it.</p>",

        "<h3>Cách Dùng Mỏ Neo Giữa Bài Quyền</h3>"
        "<p>Kiểm Tra 3 Mỏ Neo không chỉ dành cho ngồi hoặc đứng. Nó dành cho bất kỳ khoảnh khắc nào khi thực hành cảm thấy sai. Giữa bài quyền, khi chuyển động trở nên cơ khí hoặc mất tập trung, kiểm tra có ba câu hỏi nhanh:</p>"
        "<ol>"
        "<li><strong>Trọng lượng của tôi ở đâu?</strong> Câu trả lời nên chính xác (ví dụ: &ldquo;70% ở chân phải&rdquo;). Nếu bạn không thể trả lời chính xác, trọng lượng ở đâu đó bạn chưa nhận ra.</li>"
        "<li><strong>Hơi thở của tôi ở đâu?</strong> Câu trả lời nên là vị trí cụ thể (ví dụ: &ldquo;thấp trong Đan Điền&rdquo;). Nếu hơi thở cao trong ngực, thực hành đã mất sự neo.</li>"
        "<li><strong>Ý chí của tôi ở đâu?</strong> Câu trả lời nên ở thì hiện tại (ví dụ: &ldquo;trên chuyển động này&rdquo;). Nếu ý chí ở chuyển động tiếp theo hoặc ở quá khứ, thực hành đã mất sự hiện diện.</li>"
        "</ol>"
        "<p>Kiểm tra mất năm giây. Nó không làm gián đoạn thực hành; nó làm sâu nó.</p>",
    ),
    (
        "<h3>The One-Word Cue System</h3>"
        "<p>Beyond the three questions, the most distilled diagnostic is a <strong>one-word cue</strong>. This is the single word that, when repeated internally, addresses the largest current issue in the practice. Common one-word cues:</p>"
        "<ul>"
        "<li><strong>Sink</strong>: when weight is up in the chest, when breath is shallow, when tension is in the shoulders.</li>"
        "<li><strong>Open</strong>: when the kua is closed, when the chest is caved, when the joints are locked.</li>"
        "<li><strong>Yield</strong>: when the arms are pushing too hard, when the breath is held, when the mind is gripping.</li>"
        "<li><strong>Root</strong>: when the body feels floaty, when the weight is on the heels, when the ground feels uncertain.</li>"
        "<li><strong>Connect</strong>: when the form feels like separate movements, when the breath is disconnected, when the intention is fragmented.</li>"
        "</ul>"
        "<p>The one-word cue is the entire practice condensed into a single verb. It is the deepest distillation of the 3-Anchor Check.</p>",

        "<h3>Hệ Thống Câu Nhắc Một Từ</h3>"
        "<p>Vượt qua ba câu hỏi, chẩn đoán cô đọng nhất là <strong>câu nhắc một từ</strong>. Đây là từ đơn lẻ mà, khi lặp lại bên trong, giải quyết vấn đề lớn nhất hiện tại trong thực hành. Các câu nhắc một từ phổ biến:</p>"
        "<ul>"
        "<li><strong>Chìm</strong>: khi trọng lượng lên trong ngực, khi hơi thở nông, khi căng thẳng ở vai.</li>"
        "<li><strong>Mở</strong>: khi kua đóng, khi ngực sụp, khi khớp khóa.</li>"
        "<li><strong>Nhường</strong>: khi tay đẩy quá mạnh, khi hơi thở bị giữ, khi tâm đang nắm bắt.</li>"
        "<li><strong>Căn</strong>: khi cơ thể cảm thấy lơ lửng, khi trọng lượng ở gót, khi mặt đất cảm thấy không chắc.</li>"
        "<li><strong>Kết nối</strong>: khi bài quyền cảm thấy như các chuyển động riêng biệt, khi hơi thở bị ngắt kết nối, khi ý chí phân mảnh.</li>"
        "</ul>"
        "<p>Câu nhắc một từ là toàn bộ thực hành cô đọng thành một động từ duy nhất. Nó là sự chưng cất sâu nhất của Kiểm Tra 3 Mỏ Neo.</p>",
    ),
]


CO_THE_50_CONG_CU = [
    (
        "<h3>The 50+ Body and the Tennis Connection</h3>"
        "<p>The 50+ body that has spent decades playing tennis brings a particular gift to Tai Chi: the proprioceptive wisdom of a body that has done explosive movement. Tai Chi is not explosive. But the proprioceptive wisdom translates.</p>"
        "<p>A 50+ tennis player who starts Tai Chi brings: <strong>balance training</strong> from court movement; <strong>coordination</strong> from hand-eye tasks; <strong>breath awareness</strong> from match stress; <strong>kinesthetic awareness</strong> from racket feel; <strong>recoverability</strong> from post-match fatigue. Each of these has a Tai Chi equivalent that builds on rather than discards the tennis training.</p>"
        "<p>The 50+ tennis player is not a beginner to movement. They are a beginner to slow movement. The translation is from &ldquo;fast and reactive&rdquo; to &ldquo;slow and integrated&rdquo;. Once translated, the tennis player&rsquo;s movement depth often surpasses the non-tennis player within months.</p>",

        "<h3>Cơ Thể 50+ Và Kết Nối Tennis</h3>"
        "<p>Cơ thể 50+ đã dành hàng thập kỷ chơi tennis mang một món quà đặc biệt cho Thái Cực Quyền: trí tuệ cảm giác bản thể của một cơ thể đã làm chuyển động nổ. Thái Cực Quyền không nổ. Nhưng trí tuệ cảm giác bản thể chuyển đổi.</p>"
        "<p>Một người chơi tennis 50+ bắt đầu Thái Cực Quyền mang theo: <strong>tập thăng bằng</strong> từ di chuyển trên sân; <strong>phối hợp</strong> từ nhiệm vụ tay-mắt; <strong>nhận thức hơi thở</strong> từ căng thẳng trận đấu; <strong>nhận thức cảm giác</strong> từ cảm giác vợt; <strong>khả năng phục hồi</strong> từ mệt mỏi sau trận. Mỗi thứ có tương đương Thái Cực Quyền xây dựng trên thay vì loại bỏ việc tập tennis.</p>"
        "<p>Người chơi tennis 50+ không phải người mới với chuyển động. Họ là người mới với chuyển động chậm. Sự chuyển đổi là từ &ldquo;nhanh và phản ứng&rdquo; sang &ldquo;chậm và tích hợp&rdquo;. Khi đã chuyển đổi, chiều sâu chuyển động của người chơi tennis thường vượt qua người không chơi tennis trong vài tháng.</p>",
    ),
    (
        "<h3>Three Practices 50+ Bodies Benefit Most From</h3>"
        "<p>Three practices from the Tai Chi system that produce the largest measurable benefits for the 50+ body:</p>"
        "<ol>"
        "<li><strong>Five-minute Zhan Zhuang (Trụ Thế)</strong>: measurable improvement in balance within four weeks; measurable improvement in proprioception within eight weeks.</li>"
        "<li><strong>Slow 24-form practice</strong>: measurable improvement in blood pressure within twelve weeks (when combined with the breath work); measurable improvement in sleep onset latency within four weeks.</li>"
        "<li><strong>Daily 5-minute dantian breathing</strong>: measurable improvement in HRV (heart rate variability) within two weeks &mdash; a marker of parasympathetic tone and overall resilience.</li>"
        "</ol>"
        "<p>None of these requires a teacher. None requires a special outfit. None requires a studio. Each can start tomorrow, with the body as it is today, and produce the first measurable change within a month.</p>",

        "<h3>Ba Thực Hành Cơ Thể 50+ Được Lợi Nhiều Nhất</h3>"
        "<p>Ba thực hành từ hệ thống Thái Cực Quyền tạo ra lợi ích có thể đo lường lớn nhất cho cơ thể 50+:</p>"
        "<ol>"
        "<li><strong>Năm phút Trụ Thế</strong>: cải thiện thăng bằng có thể đo lường trong bốn tuần; cải thiện cảm giác bản thể có thể đo lường trong tám tuần.</li>"
        "<li><strong>Thực hành 24 thức chậm</strong>: cải thiện huyết áp có thể đo lường trong mười hai tuần (khi kết hợp với công việc hơi thở); cải thiện thời gian vào giấc ngủ có thể đo lường trong bốn tuần.</li>"
        "<li><strong>Thở Đan Điền 5 phút hằng ngày</strong>: cải thiện HRV (biến thiên nhịp tim) có thể đo lường trong hai tuần &mdash; một dấu hiệu của trương lực phó giao cảm và sức bền tổng thể.</li>"
        "</ol>"
        "<p>Không cái nào trong số này yêu cầu thầy. Không yêu cầu trang phục đặc biệt. Không yêu cầu studio. Mỗi cái có thể bắt đầu ngày mai, với cơ thể như nó hôm nay, và tạo ra sự thay đổi có thể đo lường đầu tiên trong một tháng.</p>",
    ),
]

PENG = [
    (
        '<h3>When Peng Becomes Visible</h3><p>Beginners often feel Peng as a vague &ldquo;ball&rdquo; but cannot demonstrate it. The transition from feeling to showing usually takes 2&ndash;3 months of daily practice. The visible signs: a partner pushes on your arm and your structure yields <em>slightly</em> before springing back; the arm looks soft but the foot is anchored; the breath is even; the eyes are calm.</p><p>Once visible, Peng becomes a diagnostic tool. If your structure starts to look rigid, you have left Peng and entered muscular holding. Return by releasing the shoulders, sinking the elbows, and re-grounding the feet.</p>',
        '<h3>Khi Nào Phòng Trở Nên Nhìn Thấy Được</h3><p>Người mới thường cảm nhận Phòng như một &ldquo;quả cầu&rdquo; mơ hồ nhưng không thể thể hiện. Sự chuyển tiếp thường mất 2&ndash;3 tháng thực hành hằng ngày. Dấu hiệu nhìn thấy được: đối tác đẩy tay bạn và cấu trúc <em>hơi</em> nhườn trước khi bật lại; tay trông mềm nhưng chân neo chặt; hơi thở đều; mắt bình thản.</p><p>Khi đã nhìn thấy được, Phòng trở thành công cụ chẩn đoán. Nếu cấu trúc bắt đầu trông cứng, bạn đã rời Phòng. Quay lại bằng cách thả vai, hạ khuỷu, và neo lại chân.</p>',
    ),
    (
        '<h3>Three Tests for Peng</h3><ol><li><strong>Solo test</strong>: stand in Wuji stance, raise arms to shoulder height with palms down, ask a partner to press a fingertip under each wrist <em>up</em>. The wrist should rise, not collapse.</li><li><strong>Single-direction test</strong>: have a partner push the shoulder from the side. Force should travel through your arm into the back foot.</li><li><strong>Multi-directional test</strong>: have a partner push from three directions in quick succession. The body should remain anchored.</li></ol>',
        '<h3>Ba Kiểm Tra Phòng</h3><ol><li><strong>Một mình</strong>: đứng Vô Cực, nâng tay ngang vai lòng xuống, nhờ đối tác ấn ngón tay dưới cổ tay <em>lên</em>. Cổ tay nên nâng, không sụp.</li><li><strong>Một hướng</strong>: đối tác đẩy vai từ bên. Lực nên đi qua cánh tay vào chân sau.</li><li><strong>Đa hướng</strong>: đối tác đẩy ba hướng nhanh. Cơ thể nên giữ neo.</li></ol>',
    ),
]

JI = [
    (
        '<h3>Ji vs Press in External Arts</h3><p>In boxing, a &ldquo;press&rdquo; is a chest-and-shoulder action: the upper body drives the arms forward. In Tai Chi, Ji is the <em>opposite sequence</em>: feet &rarr; legs &rarr; hips &rarr; waist &rarr; back &rarr; shoulders &rarr; arms &rarr; hands. The arms are the last thing to move.</p><p>This is why Ji is so disorienting to receive. It does not arrive like a push (which the body can brace against). It arrives like a wave (which the body must absorb or yield to).</p>',
        '<h3>Tỳ vs Đẩy Trong Võ Thuật Ngoại</h3><p>Trong boxing, &ldquo;đẩy&rdquo; là hành động ngực-vai: thân trên lái tay tới. Trong Thái Cực Quyền, Tỳ là <em>trình tự ngược lại</em>: chân &rarr; hông &rarr; eo &rarr; lưng &rarr; vai &rarr; tay &rarr; bàn tay.</p><p>Đây là lý do Tỳ gây mất phương hướng cho người nhận. Nó không đến như cú đẩy (chống lại được); nó đến như con sóng (phải hấp thụ).</p>',
    ),
    (
        '<h3>Common Errors in Ji</h3><p><strong>Pressing with arms</strong>: tie the press to a forward step &mdash; if the step does not happen, the press does not. <strong>Pressing with upper back</strong>: lead with the dantian, not the shoulders. <strong>Pressing with held breath</strong>: exhale through the press.</p>',
        '<h3>Lỗi Phổ Biến Trong Tỳ</h3><p><strong>Ép bằng tay</strong>: buộc cú ép vào bước tới. <strong>Ép bằng lưng trên</strong>: dẫn bằng Đan Điền. <strong>Ép với hơi thở bị giữ</strong>: thở ra qua cú ép.</p>',
    ),
]

AN = [
    (
        "<h3>An in Grasp Bird's Tail</h3><p>An is rarely taught in isolation. It is the fourth movement of the Grasp Bird's Tail sequence &mdash; the most studied passage in the Yang form. The four movements (Peng, Lu, Ji, An) teach the full grammar of Tai Chi interaction: receive, redirect, compress, finish.</p><p>When An is taught inside the sequence, students learn it is not a separate &ldquo;push&rdquo; but a <em>resolution</em>. The compression of Ji already contains An.</p>",
        '<h3>Án Trong Lãm Tước Vỹ</h3><p>Án hiếm khi được dạy riêng. Đó là chuyển động thứ tư của Lãm Tước Vỹ &mdash; đoạn nghiên cứu nhiều nhất trong bài Dương. Bốn chuyển động (Phòng, Lỹ, Tỳ, Án) dạy ngữ pháp: tiếp nhận, chuyển hướng, nén, kết thúc.</p><p>Khi Án được dạy trong chuỗi, học viên học rằng nó không phải cú đẩy riêng mà là <em>sự giải quyết</em>.</p>',
    ),
    (
        '<h3>An in Push Hands</h3><p>Push hands internalises An. Two people in contact; one pushes; the other receives and eventually pushes back. The common error is the &ldquo;arm-push&rdquo;: pushing with arms instead of through the ground. The correct exchange uses the centre, not the contact point.</p>',
        '<h3>Án Trong Tôi Thủ</h3><p>Tôi Thủ nội tâm hóa Án. Hai người tiếp xúc; một đẩy; người kia tiếp nhận rồi đẩy lại. Lỗi phổ biến là &ldquo;đẩy bằng tay&rdquo; thay vì qua mặt đất. Trao đổi đúng dùng trung tâm.</p>',
    ),
]

XU_THUC = [
    (
        '<h3>Xū/Shí Across the Five Styles</h3><p><strong>Chen</strong> uses large, low postures with visible weight shifts. <strong>Yang</strong> uses higher, more upright postures with subtler shifts. <strong>Wu</strong> emphasises compact, narrow steps. <strong>Wu (Hao)</strong> uses long, weighted steps with deep pauses. <strong>Sun</strong> uses high, mobile stances with frequent light-quick steps.</p>',
        '<h3>Hư/Thực Qua Năm Trường Phái</h3><p><strong>Trần</strong> dùng tư thế thấp rộng với chuyển trọng lượng nhìn thấy. <strong>Dương</strong> dùng cao hơn với chuyển dịch tinh tế. <strong>Ngô</strong> nhấn mạnh bước hẹp. <strong>Vũ</strong> dùng bước dài với dừng sâu. <strong>Tôn</strong> dùng tư thế cao, di động với bước nhẹ-nhanh.</p>',
    ),
    (
        '<h3>The Cost of Double-Loading</h3><p>The body resists single full, single empty because both feet loaded feels <em>safer</em>. The nervous system prefers certainty; Xū/Shí requires tolerating momentary instability.</p><p>The cost: joints carry double load; muscles grip continuously; nervous system stays engaged; energy dissipates. The student who masters Xū/Shí is buying back joint life, muscular relaxation, cognitive bandwidth, and energetic efficiency.</p>',
        '<h3>Chi Phí Của Song Tải</h3><p>Cơ thể chống lại một thực, một hư vì cả hai chân chịu tải cảm thấy <em>an toàn hơn</em>. Hệ thần kinh thích chắc chắn; Hư/Thực đòi hỏi chịu đựng bất ổn tạm thời.</p><p>Chi phí: khớp mang gấp đôi tải; cơ liên tục nắm; hệ thần kinh luôn gắn kết; năng lượng bị tiêu hao. Học viên thành thạo Hư/Thực mua lại tuổi thọ khớp, thư giãn cơ, băng thông nhận thức, hiệu quả năng lượng.</p>',
    ),
]


ALL_DATA = {
    "peng": PENG,
    "ji": JI,
    "an": AN,
    "xu-thuc": XU_THUC,
    "sung": SUNG,
    "sung-vs-sui": SUNG_VS_SUI,
    "yi-dan-khi": YI_DAN_KHI,
    "mushin": MUSHIN,
    "om-thu": OM_THU,
    "cham-la-nhanh": CHAM_LA_NHANH,
    "tan-hu-tan-thuc": TAN_HU_TAN_THUC,
    "nghich-tho": NGHICH_THO,
    "nam-phut-tru-the": NAM_PHUT_TRU_THE,
    "bai-30-phut": BAI_30_PHUT,
    "co-the-sau-50": CO_THE_SAU_50,
    "ba-dieu-kien-chua-lanh": BA_DIEU_KIEN_CHUA_LANH,
    "tap-20-phut-tai-nha": TAP_20_PHUT_TAI_NHA,
    "reset-5-phut": RESET_5_PHUT,
    "bay-sai-lam": BAY_SAI_LAM,
    "nghich-ly-cang": NGHICH_LY_CANG,
    "taichi-la-gi": TAICHI_LA_GI,
    "tam-bao": TAM_BAO,
    "am-duong": AM_DUONG,
    "so-do-co-the": SO_DO_CO_THE,
    "vo-vi-tru-the": VO_VI_TRU_THE,
    "lay": LAY,
    "24-thuc-tong-quat": TWENTY_FOUR_THUC_TONG_QUAT,
    "tho-dan-dien": THO_DAN_DIEN,
    "ba-mo-neo": BA_MO_NEO,
    "co-the-50-cong-cu": CO_THE_50_CONG_CU
}

if __name__ == "__main__":
    print(f"Topics with enrichment data: {len(ALL_DATA)}")