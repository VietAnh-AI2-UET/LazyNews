import streamlit as st
from core.runner import crawl_runner
from core.runner import  summary_runner

# ================== HEADER ==================
left, center, right = st.columns([1, 1, 1])
with center:
    st.title("LazyNews")

# ================== INIT STATE ==================
st.session_state.setdefault("collected", False)
st.session_state.setdefault("summarized", False)

# ================== STEP 1: COLLECT ==================
if not st.session_state.collected:
    if st.button("Thu thập"):
        with st.spinner("Đang thu thập dữ liệu..."):
            try:
                breaking = crawl_runner.run_crawl()
            except Exception as e:
                st.error(f"Lỗi khi thu thập: {e}")
                breaking = {}

        news_content_list = []
        news_title_list = []
        news_url_list = []

        for url, d in breaking.items():
            title = d.get('title', '').strip()
            main = d.get('main_content', '').strip()
            # keep original URL so summaries can use it as the document _id
            news_url_list.append(url)
            if title:
                news_title_list.append(title)
            if main:
                news_content_list.append(main)

        if not news_content_list:
            # fallback sample data if crawler returned nothing
            news_content_list = [
                "Nội dung news 01 ...",
                "Nội dung news 02 ...",
                "Nội dung news 03 ...",
                "Nội dung news 04 ...",
                "Nội dung news 05 ..."
            ]

        if not news_title_list:
            # fallback sample data if crawler returned nothing
            news_title_list = [
                "Tiêu đề news 01 ...",
                "Tiêu đề news 02 ...",
                "Tiêu đề news 03 ...",
                "Tiêu đề news 04 ...",
                "Tiêu đề news 05 ..."
            ]

        st.session_state.news_content_raw = news_content_list
        st.session_state.news_title_raw = news_title_list
        st.session_state.news_url_raw = news_url_list

        # initialize raw text widgets so behavior matches the "Thu thập lại" branch
        for i, s in enumerate(st.session_state.news_content_raw, start=1):
            st.session_state[f"raw_{i}"] = s

        st.session_state.collected = True
        st.rerun()

# ================== STEP 2: SHOW RAW NEWS ==================
else:
    if st.button("Thu thập lại"):
        st.session_state.collected = False

        with st.spinner("Đang thu thập dữ liệu..."):
            try:
                breaking = crawl_runner.run_crawl()
            except Exception as e:
                st.error(f"Lỗi khi thu thập: {e}")
                breaking = {}

        news_content_list = []
        news_title_list = []
        news_url_list = []

        for url, d in breaking.items():
            title = d.get('title', '').strip()
            main = d.get('main_content', '').strip()
            news_url_list.append(url)
            if title:
                news_title_list.append(title)
            if main:
                news_content_list.append(main)

        if not news_content_list:
            # fallback sample data if crawler returned nothing
            news_content_list = [
                "Nội dung news 01 ...",
                "Nội dung news 02 ...",
                "Nội dung news 03 ...",
                "Nội dung news 04 ...",
                "Nội dung news 05 ..."
            ]

        if not news_title_list:
            # fallback sample data if crawler returned nothing
            news_title_list = [
                "Tiêu đề news 01 ...",
                "Tiêu đề news 02 ...",
                "Tiêu đề news 03 ...",
                "Tiêu đề news 04 ...",
                "Tiêu đề news 05 ..."
            ]

        # Ghi đè trực tiếp vào session_state để bắt buộc widget hiển thị giá trị này
        st.session_state.news_content_raw = news_content_list
        st.session_state.news_title_raw = news_title_list
        st.session_state.news_url_raw = news_url_list
        for i, s in enumerate(st.session_state.news_content_raw, start=1):
            st.session_state[f"raw_{i}"] = s

        st.session_state.collected = True
        st.rerun()

    st.subheader("Tin tức thu thập")

    for i, text in enumerate(st.session_state.news_content_raw, start=1):
        if 'news_title_raw' in st.session_state and len(st.session_state.news_title_raw) >= i:
            title_label = st.session_state.news_title_raw[i-1] or f"news{i:02}"
        else:
            title_label = f"news{i:02}"

        st.text_area(
            label=title_label,
            value=text,
            key=f"raw_{i}",
            height=200
        )

    # ================== STEP 3: SUMMARIZE ==================
    if not st.session_state.summarized:
        if st.button("Tóm tắt"):
            # prepare data mapping from session lists to the expected input format
            data_for_summary = {}
            for i, content in enumerate(st.session_state.news_content_raw, start=1):
                title = st.session_state.news_title_raw[i-1] if 'news_title_raw' in st.session_state and len(st.session_state.news_title_raw) >= i else ''
                url = st.session_state.news_url_raw[i-1] if 'news_url_raw' in st.session_state and len(st.session_state.news_url_raw) >= i else f"local_{i}"
                data_for_summary[url] = {'title': title, 'main_content': content}

            try:
                breaking_summary = summary_runner.run_summary(data=data_for_summary, save_file="today_news_summary.json")
            except Exception as e:
                st.error(f"Lỗi khi tóm tắt dữ liệu: {e}")
                breaking_summary = {}

            new_title_summary = []
            new_content_summary = []

            for url, d in breaking_summary.items():
                title = d.get("title", "")
                summarization = d.get("summary", "")
                if title:
                    new_title_summary.append(title)
                if summarization:
                    new_content_summary.append(summarization)

            if not new_content_summary:
                new_content_summary = [
                    "Tóm tắt news 01 ...",
                    "Tóm tắt news 02 ...",
                    "Tóm tắt news 03 ...",
                    "Tóm tắt news 04 ...",
                    "Tóm tắt news 05 ..."
                ]

            if not new_title_summary:
                new_title_summary = [
                    "Tiêu đề news 01 ...",
                    "Tiêu đề news 02 ...",
                    "Tiêu đề news 03 ...",
                    "Tiêu đề news 04 ...",
                    "Tiêu đề news 05 ..."
                ]

            st.session_state.new_content_summary = new_content_summary
            st.session_state.new_title_summary = new_title_summary

            st.session_state.summarized = True
            st.rerun()

    # ================== STEP 4: SHOW SUMMARY ==================
    else:
        if st.button("Tóm tắt lại"):
            st.session_state.summarized = False

            # prepare data mapping from session lists to the expected input format
            data_for_summary = {}
            for i, content in enumerate(st.session_state.news_content_raw, start=1):
                title = st.session_state.news_title_raw[i-1] if 'news_title_raw' in st.session_state and len(st.session_state.news_title_raw) >= i else ''
                url = st.session_state.news_url_raw[i-1] if 'news_url_raw' in st.session_state and len(st.session_state.news_url_raw) >= i else f"local_{i}"
                data_for_summary[url] = {'title': title, 'main_content': content}

            try:
                breaking_summary = summary_runner.run_summary(data=data_for_summary, save_file="today_news_summary.json")
            except Exception as e:
                st.error(f"Lỗi khi tóm tắt dữ liệu: {e}")
                breaking_summary = {}

            new_title_summary = []
            new_content_summary = []

            for url, d in breaking_summary.items():
                title = d.get("title", "")
                summarization = d.get("summary", "")
                if title:
                    new_title_summary.append(title)
                if summarization:
                    new_content_summary.append(summarization)

            if not new_content_summary:
                new_content_summary = [
                    "Tóm tắt news 01 ...",
                    "Tóm tắt news 02 ...",
                    "Tóm tắt news 03 ...",
                    "Tóm tắt news 04 ...",
                    "Tóm tắt news 05 ..."
                ]

            if not new_title_summary:
                new_title_summary = [
                    "Tiêu đề news 01 ...",
                    "Tiêu đề news 02 ...",
                    "Tiêu đề news 03 ...",
                    "Tiêu đề news 04 ...",
                    "Tiêu đề news 05 ..."
                ]

            st.session_state.new_content_summary = new_content_summary
            st.session_state.new_title_summary = new_title_summary

            # Ghi đè trực tiếp vào session_state để bắt buộc widget hiển thị giá trị này
            for i, s in enumerate(st.session_state.new_content_summary, start=1):
                st.session_state[f"summary_{i}"] = s
                
            st.session_state.summarized = True
            st.rerun()

        st.subheader("Bản tóm tắt")

        for i, summary in enumerate(st.session_state.new_content_summary, start=1):
            if "new_title_summary" in st.session_state and len(st.session_state.new_title_summary) >= i:
                summarization_title_label = st.session_state.new_title_summary[i-1]
            else:
                summarization_title_label = f"new{i:02}"

            st.text_area(
                key=f"summary_{i}",
                label=summarization_title_label,
                value=summary,
                height=200
            )